from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('update', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('active/<uid64>/<token>', views.activate, name='activation'),
    path('login/', views.userLogin.as_view(), name='login'),
    path('verification/<int:id>/<token>', views.checkUser, name='checkUser'),
    path('logout/<int:id>/<token>', views.UserLogOut, name='logout'),
    path('user/', include(router.urls)),
    path('user/change_password/<int:id>', views.ChangePassword.as_view(), name='change password'),
]

