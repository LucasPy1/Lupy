from django.shortcuts import render, redirect
from .forms import SkillForm
from .models import SkillModel
from django.http import HttpRequest

def home(request):
    context = {
        'name':'Lucas',
        'skills':SkillModel.objects.all() 
    }
    return render(request,'user_progress/home.html', context)

def add_skills(request:HttpRequest):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_progress:home')
    
    context = {
        'form': SkillForm
    }
    return render(request,'user_progress/add_skills.html', context)

def remove_skills(request:HttpRequest):
    ...


