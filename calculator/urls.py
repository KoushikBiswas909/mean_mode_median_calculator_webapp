from django.urls import path, include

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('', views.input_data, name='inputdata'),
    path('add', views.add, name='add'),
    path("accounts/register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]
