from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import * 
  
  



class BlogForm(forms.ModelForm): 
    class Meta:  
        model = BlogModel 
        fields = [ "title", "description","image"] 

# creating a form 
class BooksForm(forms.ModelForm): 
    class Meta:  
        model = Book 
        fields = [ 
            "title", 
            "description", 
        ] 




# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']        
