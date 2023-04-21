from rest_framework import routers
from apps.account import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('profiles', views.ProfilesView, basename='profiles')
# router.register('register', views.RegisterView)

urlpatterns = [
    path('', include(router.urls)),
]







