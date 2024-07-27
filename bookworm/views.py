from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, ProfileForm

# Create your views here.
def my_blog(request):
    return HttpResponse('Hi!')

@login_required

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
