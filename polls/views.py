from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages

from .models import Question, Choice


class IndexView(generic.ListView):
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


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, *args, **kwargs):
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
            return render(request, 'polls/detail.html', {
                    'question': question, })


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # if not question.can_vote():
        #     messages.error(request, "You cannot vote this poll.")
        #     return HttpResponseRedirect(reverse('polls:index'))
        # else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
