import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Question class for create Question object.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date', null=True)

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """Check for question that was published recently, not more than 1 day."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Check if question is published compare to current time."""
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """Check of question can vote only in voting period, user cannot vote after end date."""
        now = timezone.now()
        if self.end_date is None:
            return True
        return self.pub_date <= now <= self.end_date


class Choice(models.Model):
    """
    Choice class for create choices for Question objects.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return string represent each choice."""
        return self.choice_text

#     @property
#     def votes(self):
#         """Count the number of votes for a choice."""
#         return Vote.objects.filter(choice.id=self.id).count()
#
#
# class Vote(models.Model):
#     """A Vote records a Users choice on a Poll."""
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
