from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.forms import CustomUSerCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from django.views import View


# Create your views here.
def register(request):
    form = CustomUSerCreationForm()
    if request.method == 'POST':
        form = CustomUSerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message=f'{form.cleaned_data["email"]} successfully registered')
            return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'You are already logged in as <b>{request.user.username}</b>. To switch user'
                                         f' <a href="#" data-toggle="modal" data-target="#logoutModal"></i>'
                                         f'log out here.</a>'))
        return redirect('website:index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            messages.success(request, message=f'{user.email} sucessfully logged in!')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('website:index')
        else:
            messages.warning(request, 'Could not authenticate, check credentials.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('accounts:login')

# @login_required()
# def profile(request):
#     return render(request, 'accounts/profile/profile.html')


class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'accounts/profile/profile.html', context)

    def post(self, request):
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your profile has been updated successfully')

            return render(request, 'accounts/profile/profile.html')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, 'Error updating you profile')

            return render(request, 'accounts/profile/profile.html', context)


# class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
#     template_name = 'accounts/change_password.html'
#     success_message = "Successfully Changed Your Password"
#     success_url = reverse_lazy('website:index')
