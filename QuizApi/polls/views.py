from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from .models import Question
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions':questions})

def question_detail(request, id):
    question = Question.objects.get(id=id)
    return render (request, 'question_detail.html',{'question':question})