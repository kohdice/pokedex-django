from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View

from .forms import LoginForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        """GETリクエスト用メソッド"""
        context = {"form": LoginForm()}

        return TemplateResponse(request, "accounts/login.html", context)

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用メソッド"""
        form = LoginForm(request.POST)

        if not form.is_valid():
            context = {"form": form}
            return TemplateResponse(request, "accounts/login.html", context)

        user = form.get_user()
        auth_login(request, user)

        return HttpResponseRedirect(reverse("pokedex:index"))


login = LoginView.as_view()
