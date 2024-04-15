from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('update', views.UserViewSet)

urlpatterns = [
    path('<int:id>/<token>', views.userProfile.as_view(), name='profile'),
    path('user/', include(router.urls)),
    path('user/change_password/<int:id>', views.ChangePassword.as_view(), name='change password'),   
]
