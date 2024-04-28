from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from .models import *
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions':questions})

def question_detail(request, id):
    if request.method == 'POST':
        print(request.POST)
        choice_id = request.POST.get('choice')
        choice = Choice.objects.get(id=choice_id)
        choice.count = choice.count+1
        choice.save()
    question = Question.objects.get(id=id)
    return render (request, 'question_detail.html',{'question':question})