from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from accounts.tokens import account_activation_token


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
        messages.success(request, mark_safe(f'Dear <b>{user}</b>, please go to you email <b>{user.email}</b> inbox '
                                            f'and click on received activation link to confirm and complete the '
                                            f'registration. <b>Note:</b> Check your spam folder.'))
    else:
        messages.error(request, mark_safe(f'Problem sending confirmation email to {user.email}, check if you typed it '
                                          f'correctly.'))
