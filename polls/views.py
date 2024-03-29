from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.all
    #template = loader.get_template('polls/main.html')
    context = {'latest_question_list': latest_question_list,}
    
    return render(request, 'polls/main.html', context)
    
    #return HttpResponse("hello world, you are at polls index")
    

def detail(request, question_id):
    return HttpResponse("You're looking at a question %s." %question_id)

def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id)



