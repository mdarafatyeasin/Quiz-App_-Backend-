from django.urls import path
from . import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('active/<uid64>/<token>', views.activate, name='activation'),
    path('login/', views.userLogin.as_view(), name='login'),
    path('verification/<int:id>/<token>', views.checkUser, name='checkUser'),
]

