from django.urls import path
from .views import logout_view
from .views import login_view

urlpatterns = [

	path("login", login_view),
	path("logout", logout_view),
]
