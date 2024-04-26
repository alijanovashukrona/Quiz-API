from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from .models import Question
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions':questions})
