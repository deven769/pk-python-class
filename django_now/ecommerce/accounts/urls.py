from django.urls import path
from .views import *
app_name = 'accounts'

urlpatterns = [
	path('signup/', signup, name = 'signup'),
	path('login/', user_login, name = 'login'),
]