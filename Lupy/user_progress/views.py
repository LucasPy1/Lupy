from django.shortcuts import render, redirect, get_object_or_404
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

def remove_skills(request:HttpRequest,id):
    skill = get_object_or_404(SkillModel,id=id)
    skill.delete()
    return redirect('user_progress:home')

def edit_skills(request:HttpRequest,id):
    skill = get_object_or_404(SkillModel, id=id)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('user_progress:home')
    
    form = SkillForm(instance=skill)
    context = {
        "form": form
    }
    
    return render(request,'user_progress/edit_skills.html',context)


