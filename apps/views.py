

from django.shortcuts import render, redirect
#from django.contrib.auth.forms import Authentication,UserCreationForm 
from .forms import CustomUserCreationForm
from django.contrib.auth import  authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import ContactForm



# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Utilisation de l'alias auth_login
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login.html')

@login_required
def acceuil(request):
    return render(request, 'acceuil.html')



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acceuil')  # Rediriger vers la page d'accueil après soumission réussie
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def logout(request):
    auth_logout(request)  # Utilisation de l'alias auth_login
    return redirect('login')











