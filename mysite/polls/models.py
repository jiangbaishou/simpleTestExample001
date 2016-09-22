from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	#This is to define a str method for this class
	def __str__(self):
		return self.question_text

	#for time representation
	def was_published_recently(self):
		return timezone.now() - datetime.timedelta(days = 1) <= self.pub_date <= timezone.now()

	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	def __str__(self):
		return self.choice_text

	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

