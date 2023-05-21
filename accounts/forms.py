from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
    )
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            validate_email(email)
            return email
        except ValueError:
            raise forms.ValidationError("正しいメールアドレスを入力してください。", code="invalid")

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("正しいメールアドレスを入力してください。")

        if not user.check_password(password):
            raise forms.ValidationError("正しいパスワードを入力してください。")

        return super().clean()
