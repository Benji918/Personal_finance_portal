from django.urls import path
from accounts import views
from accounts.views import MyProfile
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
# from accounts.views import ChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', MyProfile.as_view(), name='profile'),

    # Password_Reset
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='accounts/password-reset/password_reset.html',
             html_email_template_name='accounts/password-reset/password_reset_email.html'
         ),
         name='password-reset'
         ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password-reset'
                                                                             '/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password-reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password-reset/password_reset_complete.html'),
         name='password_reset_complete'),

    # change_password
    # path('password_change/', ChangePasswordView.as_view(), name='password_change'),

]
