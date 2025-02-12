from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import CustomUserCreationForm

from entries.models import Entry

# Create your views here.

def register_view(request):
   if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
        
      if form.is_valid():
         # Save the new user. making sure that the username is all lower case, ensure data integrity
         # user = form.save(commit = False)
         # user.username = user.username.lower()
         # user.save
         #alternatively, just save, the checks will be done by form.is_valid() in the login_view
         user = form.save()
         login(request, user)
         # Show a success message
         messages.success(request, 'Your account has been created successfully. Welcome')
         # Redirect to the login page (or any other page)
         return redirect('home')
      else:
         # Show error messages if the form is invalid
         messages.error(request, 'There was an error creating your account. Please try again.')
   # first access to /register will be a get, and will execute the else pathway
   else:
      form = CustomUserCreationForm()
   return render(request, 'login_register.html', {'form': form})


def login_view(request):
   if request.method == 'POST':
      # Authentication form only works if input is username and password
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         # Get 'next' parameter or default to '/entries/' if not provided
         next_url = request.POST.get('next') or request.GET.get('next') or 'home'
         # Redirect to the next URL
         return redirect(next_url)
      else:
         # If the form is not valid (wrong credentials), show error messages
            for error in form.errors.get('__all__', []):  # Get general errors from the form
               messages.error(request, error)
            return redirect('login_view')  # Redirect back to login if errors exist
   else:
      form = AuthenticationForm()
   context = {'form': form}
   return render(request, 'login_login.html', context)


def logout_view(request):
   logout(request)
   return redirect('home')


def profile_view(request):
   user = request.user
   entries = user.entry_set.all()
   context = {'user': user,
              'entries': entries,
              'entry_count': entries.count()}
   return render(request, 'user_profile.html', context)
