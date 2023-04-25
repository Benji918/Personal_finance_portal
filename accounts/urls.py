from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('sms_verify/<int:user_id>/', views.sms_verification_view, name='sms_verify'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('delete/', views.delete_user_account, name='delete'),
    # password change
    path("password_change/", views.password_change, name="password_change"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
]

