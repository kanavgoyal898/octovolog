from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account updated for {username}.')
            return redirect('profile') 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)