from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('question/<int:id>', question_detail, name = 'question_detail')
]