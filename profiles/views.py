from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile
from .forms import Profile, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def userProfile(request, pk):
    profile = Profile.objects.get(user=pk)
    context = {'profile': profile}
    return render(request, 'bookworm/register.html', context)

def register(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = userprofile.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = NewUserForm()
        profile_form = ProfileForm()
    return render(request, 'readit/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile_update(request):
    user = request.user
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'readit/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})
