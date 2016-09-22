from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404

# Create your views here.
#index view
def index(request):
	"""
	I prefer writing descrption for a view function here inside a function prototype.
	"""
	#return HttpResponse("Hello, world. You are at the polls index, Mr.Zhang, congratulations.")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	#output = ', '.join([q.question_text for q in latest_question_list])
	return render(request, 'polls/index.html', context)
#end of index


#detail view
def detail(request, question_id):
	#try:
		#return HttpResponse("You're looking at question %s." % question_id)
		#question = Question.objects.get(pk = question_id)
	#except Question.DoesNotExist:
		#raise Http404('Question does not exist')
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})


#results view
def results(request, question_id):
	#response = "You're looking at the results of question %s."
	#return HttpResponse(response % question_id)
	question  = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})


#vote view
def vote(request, question_id):
	#return HttpResponse("You are voting on question %s." % question_id)
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['cjpoce'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice',})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))

