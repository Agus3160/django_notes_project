from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm

urlpatterns = [
  
  #Protected routes
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('add', views.add, name='add'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('sign-out', views.signOut, name='sign-out'),

  #Public routes
  path('sign-up', views.signUp, name='sign-up'),
  path('sign-in', views.signIn, name='sign-in'),

  #Reset password
  path('password-reset', auth_views.PasswordResetView.as_view(template_name='reset-password/password_reset_form.html', form_class=CustomPasswordResetForm, email_template_name='reset-password/password_reset_email.html'), name='password-reset'),
  path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='reset-password/password_reset_done.html'), name='password_reset_done'),
  path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset-password/password_reset_confirm.html', success_url='/password-reset/complete'), name='password-reset-confirm'),
  path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='reset-password/password_reset_complete.html'), name='password-reset-complete'),

  
]