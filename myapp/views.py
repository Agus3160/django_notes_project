from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNoteForm, SignUpForm, LoginForm
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .custom.decorators import kick_auth_auth_users
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def index(request):
  notes = Note.objects.all().filter(user=request.user)
  noteslist = list(notes)
  return render(request, 'index.html', {'notes': noteslist})

def about(request):
  return render(request, 'about.html')

def add(request):
  if request.method == 'POST':
    form = AddNoteForm(request.POST)
    if form.is_valid():
      note = form.save(commit=False)
      note.user = request.user
      form.save()
      return redirect('index')
  else:
    form = AddNoteForm()
  return render(request, 'add.html', {'form': form})

def delete(request, id):
  if request.method == 'POST':
    note = get_object_or_404(Note, id=id, user = request.user)
    note.delete()
    return redirect('index')
  else:
    return HttpResponseBadRequest(JsonResponse({'success': False, 'message': 'Bad request'}), content_type="application/json")
  
def edit(request, id):
    if request.method == 'POST':
      note = Note.objects.get(id=id)
      form = AddNoteForm(request.POST, instance=note)
      if form.is_valid():
        form.save()
        return redirect('index')
    else:
      note = Note.objects.get(id=id)
      form = AddNoteForm(instance=note) 
    return render(request, 'edit.html', {'form': form, 'note': note})

@kick_auth_auth_users(redirect_to='/')
def signUp(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/sign-in')
  else:
    form = SignUpForm()
  return render(request, 'sign-up.html', {'form': form})

@kick_auth_auth_users(redirect_to='/')
def signIn(request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active:
      login(request, user)
      return redirect('/')
    else:
      form.add_error(None, "Invalid username or password.")
  return render(request, 'sign-in.html', {'form': form})


def signOut(request):
  logout(request)
  return redirect('/sign-in')