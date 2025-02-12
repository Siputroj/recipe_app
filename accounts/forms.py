from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
   email = forms.EmailField(required=True)
   first_name = forms.CharField(max_length=30)
   last_name = forms.CharField(max_length=30)
   
   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


   # all the clean functions are automatically run when doing .is_valid() method
   def clean_username(self):
      username = self.cleaned_data.get('username')

      if User.objects.filter(username = username).exists():
         raise ValidationError("This username is already in use")
      return username

   def clean_email(self):
      email = self.cleaned_data.get('email')
      #cleaned_data does not check for duplicates
      if User.objects.filter(email = email).exists():
         raise ValidationError("This email address is already in use")
      return email

   def clean_first_name(self):
      first_name = self.cleaned_data.get('first_name')
      if len(first_name) < 2:
         raise ValidationError("First name must be atleast 2 characters.")
      if any(char.isdigit() for char in first_name):
         raise ValidationError("First name cannot contain numeric values.")
      return first_name
      
   def clean_last_name(self):
      last_name = self.cleaned_data.get('last_name')
      if len(last_name) < 2:
         raise ValidationError("First name must be atleast 2 characters.")
      if any(char.isdigit() for char in last_name):
         raise ValidationError("First name cannot contain numeric values.")
      return last_name