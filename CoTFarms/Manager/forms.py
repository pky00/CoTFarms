from django import forms
from .models import CowType, Cow, CowMilking, CowMilkSale, CowPregnancy
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date



def pkExists(val):
    if Cow.objects.filter(pk=val):
        raise ValidationError(
            _('%(value)s is an existing Cow ID'),
            params={'value': val},
        )

class addCowForm(forms.ModelForm):
    Gender = (("M","MALE"),("F","FEMALE"))

    number = forms.IntegerField(label="Cow ID", required=True, help_text="Must be Unique", validators=[pkExists])
    dob = forms.DateField(label="Date of Birth", required=True, help_text="Format : YYYY-MM-DD !!!Anything else won't work!!!")
    Type = forms.ModelChoiceField(label="Type",queryset=CowType.objects.all(), required=True)
    mother = forms.ModelChoiceField(label="Mother",queryset=Cow.objects.filter(dead=False,gender="F"))
    gender = forms.ChoiceField(label="Gender", choices=Gender, required=True)
    dead = forms.BooleanField(label="Dead", required=False)
    isMilking = forms.BooleanField(label="Milking", required=False)

    class Meta:
        model = Cow
        fields = ['number', 'dob', 'Type', 'mother', 'gender', 'dead', 'isMilking']


class editCowForm(forms.ModelForm):
    Gender = (("M","MALE"),("F","FEMALE"))

    number = forms.IntegerField(label="Cow ID", required=False, help_text="Must be Unique", disabled=True)
    dob = forms.DateField(label="Date of Birth", required=True, help_text="Format : YYYY-MM-DD !!!Anything else won't work!!!")
    Type = forms.ModelChoiceField(label="Type",queryset=CowType.objects.all(), required=True)
    mother = forms.ModelChoiceField(label="Mother",queryset=Cow.objects.filter(dead=False), required=False)
    gender = forms.ChoiceField(label="Gender", choices=Gender, required=True)
    dead = forms.BooleanField(label="Dead", required=False)
    isMilking = forms.BooleanField(label="Milking", required=False)

    class Meta:
        model = Cow
        fields = ['number', 'dob', 'Type', 'mother', 'gender', 'dead', 'isMilking']

class addCowMilkForm(forms.ModelForm):
    cow = forms.ModelChoiceField(label="Cow",required=True,queryset=Cow.objects.filter(dead=False,isMilking=True))
    amount = forms.FloatField(label="Amount",required=True, help_text="Unit : Kg")
    date = forms.DateTimeField(label="Date",required=True, help_text="Format : YYYY-MM-DD", initial=date.today)

    class Meta:
        model = CowMilking
        fields = ['cow','amount','date']

class addCowMilkSaleForm(forms.ModelForm):
    amount = forms.IntegerField(label="Amount" ,required=True ,help_text="Unit : Kg")
    date = forms.DateTimeField(label="Date" ,required=True ,initial=date.today)
    price = forms.FloatField(label="Price" ,required=True ,help_text="Unit : LBP")

    class Meta:
        model = CowMilkSale
        fields = ['amount','date','price']

class addCowPregnancyForm(forms.ModelForm):
    cow = forms.ModelChoiceField(label="Cow",required=True,queryset=Cow.objects.filter(dead=False,gender='F'))
    dop = forms.DateTimeField(label="Date of Pregnancy",required=True,initial=date.today) #date of pregnancy
    success = forms.BooleanField(label="Success",required=False)
    child = forms.ModelChoiceField(label="Child",required=False,queryset=Cow.objects.filter(dead=False))

    class Meta:
        model = CowPregnancy
        fields = ['cow','dop','success','child']