from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("test", views.test, name="test"),
    path("formas", views.formas, name='formas' )
]