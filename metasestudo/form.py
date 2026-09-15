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

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email
