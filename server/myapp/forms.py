from django import forms
from .models import StudentModel,Movie

class studentform(forms.Form):
  name= forms.CharField(label= "Student Name:",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
  email=forms.EmailField(label="Email:",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
  password=forms.CharField(label="Password:",widget=forms.PasswordInput(attrs={"class":"form-control"}))
  confirm_pass=forms.CharField(label="Repete Password",widget=forms.PasswordInput(attrs={"class": "form-control"}))
  check= forms.BooleanField(label="Agree:",required=True,disabled=False, widget=forms.widgets.CheckboxInput(attrs={'class':'checkbox-in'}))
  


class StudentModelform(forms.ModelForm):
  class Meta:
    model=StudentModel
    fields= '__all__'
    widgets={
      'name':forms.TextInput(attrs={"class":"form-control"}),
      'email':forms.TextInput(attrs={"class":"form-control"}),
      'password':forms.PasswordInput(attrs={"class":"form-control"}),
      'confirm_pass':forms.PasswordInput(attrs={"class":"form-control"}),
    }
    
class MovieForm(forms.ModelForm):
  class Meta:
    model=Movie
    fields= '__all__'
  
  
class LoginForm(forms.Form):
  username= forms.CharField(label= "Student Name:",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
  password=forms.CharField(label="Password:",widget=forms.PasswordInput(attrs={"class":"form-control"}))