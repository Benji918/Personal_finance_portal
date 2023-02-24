from django.urls import path
from accounts import views
from accounts.views import MyProfile


app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', MyProfile.as_view(), name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # password change
    path("password_change/", views.password_change, name="password_change"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
]

