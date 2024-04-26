from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

class Choice(models.Model):
    text = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

