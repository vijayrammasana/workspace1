from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def index(request):
    return render(request,'first_app/index.html')

def form_name_view(request):
    form = forms.Forname()
    return render(request,'first_app/form_page.html',{'form' :form})
