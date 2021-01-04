from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import addCowForm, editCowForm, addCowMilkForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from datetime import date
from django.shortcuts import redirect

@login_required
def CowMilk(request):

    today = date.today()
    milkings = CowMilking.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)

    if request.method == 'POST' :
        addForm = addCowMilkForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            addForm = addCowMilkForm()
    else:
        addForm = addCowMilkForm()

    context = {
        'milkings': milkings,
        'addForm': addForm,
    }   

    return render(request, 'Manager/CowMilk.html', context)

@login_required
def CowMilkDelete(request,deleteID=None):
    CowMilking.objects.get(id=deleteID).delete()
    return redirect("manager-cow-milk")


# Create your views here.
class CowListView(ListView):
    model = Cow
    template_name = 'Manager/Cows.html'
    context_object_name = "cows"
    ordering = ['number']
    paginate_by = 8


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

