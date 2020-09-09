from .  import views
from django.urls  import path, include

urlpatterns = [
    path('todo', views.todo, name = 'todo'),
    path('Favorite', views.favorite, name = 'Favorite')
]
