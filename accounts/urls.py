from django.urls import include, path

from . import views

app_name = "accounts"
urlpatterns = [path("login/", views.login, name="login")]
