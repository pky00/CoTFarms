from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import addCowForm, editCowForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):

    context = {
        'cows': Cow.objects.all(),
    }

    return render(request, 'Manager/Cows.html', context)


@login_required
def AddCow(request):

    added = False
    cowID = 0

    if request.method == 'POST' :
        addForm = addCowForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            added = True
            cowID = addForm.cleaned_data['number']
            addForm = addCowForm()
    else:
        addForm = addCowForm()

    context = {
        'addForm': addForm,
        'added' : added,
        'cowID' : cowID,

    }

    return render(request, 'Manager/AddCow.html', context)


@login_required
def EditCow(request,cowID):

    cow = Cow.objects.get(pk=cowID)
    if request.method == 'POST' :
        editForm = editCowForm(request.POST, instance=cow)
        if editForm.is_valid():
            editForm.save()
            return HttpResponseRedirect('..')
    else:
        editForm = editCowForm(instance=cow)

    context = {
        'editForm': editForm
    }

    return render(request, 'Manager/EditCow.html', context)    

