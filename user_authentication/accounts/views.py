from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm



# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#configuring signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            full_name = form.cleaned_data['Full Name']
            email = form.cleaned_data['Email Address']
            password = form.cleaned_data['Password']
            confirm_password = form.cleaned_data['Confirm Password']
            if password == confirm_password:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = full_name
                user.save()
                login(request, user)
                return redirect('home')  # Redirect to home or any other page
            else:
                form.add_error('confirm_password', 'Passwords do not match')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
