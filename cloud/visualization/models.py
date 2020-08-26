from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date  <= now
