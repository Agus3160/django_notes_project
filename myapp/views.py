from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNoteForm, SignUpForm
from django.http import JsonResponse

# Create your views here.
def index(request):
  notes = Note.objects.all()
  noteslist = list(notes)
  return render(request, 'index.html', {'notes': noteslist})

def about(request):
  return render(request, 'about.html')

def add(request):
  if request.method == 'POST':
    form = AddNoteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = AddNoteForm()
  return render(request, 'add.html', {'form': form})

def delete(request, id):
  if request.method != 'POST':
    return JsonResponse(
      {
        'success': False,
        'message': 'DELETE request required'
      }
    )
  note = Note.objects.get(id=id)
  note.delete()
  return redirect('index')

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

def signUp(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = SignUpForm()
  return render(request, 'sign-up.html', {'form': form})

def signIn(request):
  return render(request, 'sign-in.html')