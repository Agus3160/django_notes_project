from django.urls import path
from . import views

urlpatterns = [
  
  #Protected routes
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('add', views.add, name='add'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('edit/<int:id>', views.edit, name='edit'),

  #Public routes
  path('sign-up', views.signUp, name='sign-up'),
  path('sign-in', views.signIn, name='sign-in'),
  
]