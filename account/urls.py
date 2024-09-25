from django.urls import path
from .views import register, login_user, logout_user, profile_view, update_profile
urlpatterns = [
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('profile', profile_view, name='profile' ),
    path('profile/change', update_profile, name='changeProfile'),
]