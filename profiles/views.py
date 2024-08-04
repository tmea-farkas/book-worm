from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

def profile_redirect(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return redirect('profile', pk=profile.id)

@login_required
def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.user == profile.user:
        profile.delete()
        #to create blank profile
        user_profile = Profile(user=request.user)
        user_profile.save()
        message.success(request, 'Your profile has been deleted!')
    return redirect('profile', pk=profile.id)


@login_required
def profile_update(request):
    print('hello')
    user = request.user
    profile = Profile.objects.get(user=user)
    # if not hasattr(user, 'profile'):
    #     Profile.objects.create(user=user)

    if request.method == 'POST':
        if request.user == profile.user:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                form = profile_form.save(commit=False)
                form.user = user
                form.save()
                messages.success(request, 'Profile update successful!')
                return redirect('profile', pk=profile.id)
            else:
                messages.error(request, 'Failed to update profile. Please ensure the form was filled out correctly.')
                return redirect('home')
        else:
            messages.error(request, 'You are not authorized to edit this profile.')
            return redirect('home')
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_update.html', {'profile_form': profile_form})
