from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                profile_picture=form.cleaned_data.get('profile_picture'),
                address_line1=form.cleaned_data.get('address_line1'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                pincode=form.cleaned_data.get('pincode'),
                user_type=form.cleaned_data.get('user_type'),
            )
            profile.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, 'users/dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/dashboard/')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'profile': request.user.profile})

def index(request):
    return render(request, 'users/index.html')
