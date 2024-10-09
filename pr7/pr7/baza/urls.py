from django.urls import path
from .views import get_base
from .views import o_nas

urlpatterns = [
path('', get_base),
path('onas/', o_nas, name='onas'),
]