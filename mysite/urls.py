from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from listasApp import views
from .views import login
from rest_framework.authtoken import views as rest_framework_views

router = routers.DefaultRouter()
router.register('Listas', views.ListaViewSet, 'lista')
router.register('users',views.UserViewSet,'user')
router.register('users',views.ProductoViewSet,'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/auth/', include('knox.urls')),
    url("^", include(router.urls)),
    url("^auth/register/$", views.RegistrationAPI.as_view()),
    url("^auth/login/$", views.LoginAPI.as_view()),
    url("^auth/user/$", views.UserAPI.as_view()),
    url("^login/$", login),
]
