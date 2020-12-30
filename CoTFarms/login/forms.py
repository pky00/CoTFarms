from django import forms

class loginForm(forms.Form):
    username = forms.CharField(required=True)
    passworrd = forms.CharField(required=True,widget=forms.PasswordInput)