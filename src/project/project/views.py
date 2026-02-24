from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PromptForm
from services.ollama_service import OllamaService

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
        
    return render(request, "registration/registration.html", {"form": form})

def prompt(request):
    if request.method == "POST":
        form = PromptForm(request.POST)
        
        if form.is_valid():
            service = OllamaService()
            
            prompt = form.cleaned_data["prompt"]
            response = service.get_response(prompt)
            
            print(response)
            
            return render(request, "prompt-form.html", {"form": form, "response": response})
    else:
        form = PromptForm()
    
    return render(request, "prompt-form.html", {"form": form})
