from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Question, Choice, Vote


class IndexView(generic.ListView):
    """
    Index view for list of poll questions.
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    View for details of question including choices.
    """
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, *args, **kwargs):
        """
        Redirect to detail page if poll is unavailable for voting.
        """
        try:
            # question = get_object_or_404(Question, pk=kwargs['pk'])
            question = Question.objects.get(pk=kwargs['pk'])
            if not question.is_published():
                messages.error(request, 'Poll is unpublished.')
                return HttpResponseRedirect(reverse('polls:index'))
            if not question.can_vote():
                messages.error(request, 'Voting are not allow.')
                return HttpResponseRedirect(reverse('polls:index'))
        except Question.DoesNotExist:
            messages.error(request, 'This poll is invalid.')
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            try:
                all_choice = question.choice_set.all()
                user_vote = Vote.objects.get(user=request.user,
                                             choice__in=all_choice).choice
            except Vote.DoesNotExist:
                user_vote = ''
            return render(request, 'polls/detail.html', {
                    'question': question,
                    'voted': user_vote, })


class ResultsView(generic.DetailView):
    """
    View for results of question.
    """
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    """
    Record the vote when user submit it.
    """
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if not question.can_vote():
            messages.error(request, "You cannot vote this poll.")
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            # selected_choice.votes += 1
            # selected_choice.save()
            # return HttpResponseRedirect(reverse('polls:results',
            #                                     args=(question.id,)))
            try:
                # get vote from previous vote if it already existed.
                current_vote = Vote.objects.get(user=request.user,
                                                choice__question=question_id)
            except Vote.DoesNotExist:
                current_vote = Vote.objects.create(user=request.user,
                                                   choice=selected_choice)
            # save vote with selected choice
            current_vote.choice = selected_choice
            current_vote.save()

            return HttpResponseRedirect(reverse('polls:results',
                                                args=(question.id,)))


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
            # return redirect('polls')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
