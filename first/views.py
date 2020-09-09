from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from .models import Scores

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def students(request):

    students = Students.objects.all()

    return render(request, 'first/students.html', {
        'text' : '안녕하세요',
        'students' : students
    })

def scores(request):

    scores = Scores.objects.all()
    print(scores)
    return render(request, 'first/scores.html' )\
        