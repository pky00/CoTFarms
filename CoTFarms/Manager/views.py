from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import addCowForm, editCowForm, addCowMilkForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from datetime import date
from django.core.paginator import Paginator
from django.db.models import Avg, Sum, Max, Min

@login_required
def CowMilk(request):

    if request.method == 'POST' :
        addForm = addCowMilkForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            addForm = addCowMilkForm()
    else:
        addForm = addCowMilkForm()

    today = date.today()
    milkings = CowMilking.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day).order_by('-amount')

    paginator = Paginator(milkings, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    avg = int(list(milkings.aggregate(Avg('amount')).values())[0])
    sum = int(list(milkings.aggregate(Sum('amount')).values())[0])
    max = int(list(milkings.aggregate(Max('amount')).values())[0])
    min = int(list(milkings.aggregate(Min('amount')).values())[0])
    number = milkings.count()


    context = {
        'milkings': page_obj,
        'addForm': addForm,
        'avg': avg,
        'sum': sum,
        'max': max,
        'min': min,
        'number': number,
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

