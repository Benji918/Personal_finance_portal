from babel._compat import force_text
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import Http404
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import Set_Password_Form
from .forms import Password_Reset_Form
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from accounts.forms import CustomUSerCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from .tokens import account_activation_token

# Create your views here.
def register(request):
    form = CustomUSerCreationForm()
    if request.method == 'POST':
        form = CustomUSerCreationForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # Send activation email
            send_activation_email(request, user)
            return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('website:index')

def send_activation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Activate Your Account'
    message = render_to_string('accounts/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(
        subject, message, to=[user.email]
    )
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{user.email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {user.email}, check if you typed it correctly.')


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

            return render(request, 'templates/base2d.html', context)


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = Set_Password_Form(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('accounts:login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = Set_Password_Form(user)
    return render(request, 'accounts/password-reset/password_reset_confirm.html', {'form': form})


def password_reset_request(request):
    if request.method == 'POST':
        form = Password_Reset_Form(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = User.objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password User Reset request"
                message = render_to_string("accounts/password-reset/password_reset_email.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                # email = EmailMessage(subject, message, to=[associated_user.email])
                print(settings.EMAIL_HOST_USER)
                email = send_mail(subject=subject, from_email=settings.EMAIL_HOST_USER, message=message,
                                  recipient_list=[associated_user.email])
                if email:
                    messages.success(request,
                                     """
                                     <h2>Password reset sent</h2><hr>
                                     <p>
                                         We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                                         You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                                         you registered with, and check your spam folder.
                                     </p>
                                     """
                                     )
                    messages.success(request, "Email Sent Successfully. Check your inbox!")
                    return redirect('website:index')
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            else:
                messages.error(request, "Invalid email address. Try again!")
                return redirect('accounts:password_reset')

        for error in list(form.errors.values()):
            messages.error(request, error)

    form = Password_Reset_Form()
    return render(
        request=request,
        template_name="accounts/password-reset/password_reset.html",
        context={"form": form}
    )


def passwordResetConfirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = Set_Password_Form(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('website:index')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = Set_Password_Form(user)
        return render(request, 'accounts/password-reset/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("accounts.login")
