from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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
def profile_update(request):
    user = request.user
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profiles/profile_update.html', {'profile_form': profile_form})
