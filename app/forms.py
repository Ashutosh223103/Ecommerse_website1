from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Customer
from django.contrib.auth import password_validation
from .models import Contact,PropertyListing
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'selling_price': forms.TextInput(attrs={'class': 'form-control'}),
                   'discounted_price': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'brand': forms.TextInput(attrs={'class': 'form-control'}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   }



class CustomerRegistrationForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'email', 'password1', 'password2']
  labels = {'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
 old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True,  'class':'form-control'}))
 new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
 new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
 email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
 new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
 new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name', 'locality', 'city', 'state', 'zipcode']
    widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}), 'city':forms.TextInput(attrs={'class':'form-control'}), 
    'state':forms.Select(attrs={'class':'form-control'}),
    'zipcode':forms.NumberInput(attrs={'class':'form-control'})}



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}), }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ['title', 'description', 'price', 'bedrooms', 'bathrooms', 'address', 'city', 'state', 'country', 'zipcode', 'image']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'class': 'form-control'}),
                   'bedrooms': forms.TextInput(attrs={'class': 'form-control'}),
                   'bathrooms': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'state': forms.TextInput(attrs={'class': 'form-control'}),
                   'country': forms.TextInput(attrs={'class': 'form-control'}),
                   'zipcode': forms.TextInput(attrs={'class': 'form-control'}),}
