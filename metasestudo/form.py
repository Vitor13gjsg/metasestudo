from django import forms    
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class CadastroForm(UserCreationForm):
    email = forms.EmailField(
      required=True,
      widget=forms.EmailInput(attrs={
          "placeholder": "E-mail", 
          "autoComplete": "email",
     })
    )
      
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].error_messages["required"] = "Informe um nome de usuário."
        self.fields["email"].error_messages["required"] = "Informe um e-mail."
        self.fields["email"].error_messages["invalid"] = "Digite um e-mail válido."
        self.fields["password1"].error_messages["required"] = "Informe uma senha."
        self.fields["password2"].error_messages["required"] = "Confirme sua senha."
        self.fields["password2"].error_messages["password_mismatch"] = "As senhas não coincidem."

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "E-mail",
            "autoComplete": "email",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Senha",
            "autoComplete": "current-password",
        })
    )
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("E-mail ou senha inválidos.")

            if not user.check_password(password):
                raise forms.ValidationError("E-mail ou senha inválidos.")
            
            if not user.is_active:
                raise forms.ValidationError("Esta conta está inativa.")
            
            self.user = user
            
        return cleaned_data
    def get_user(self):
        return self.user