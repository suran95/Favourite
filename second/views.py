from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .models import Favorite

# Create your views here.
def index(request):
   
    return render(request, 'second/index.html')

def todo(request):

    todo = Todo.objects.all()
    return render(request, 'second/todo.html', {'todos' : todo} )

def favorite(request):

    favorite = Favorite.objects.all()
    return render(request, 'second/favorite.html', {'favorites' : favorite} )
