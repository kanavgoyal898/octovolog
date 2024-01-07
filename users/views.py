from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Log in!')
            return redirect('login') 
    else:
        form = {'form' : UserRegisterForm()}
    return render(request, 'users/register.html', form)

@login_required
def profile(request):
    return render(request, 'users/profile.html')