from django import forms
from home.models import Student

class StudentForm(forms.Form):
  name = forms.CharField(max_length=50)
  phone = forms.CharField()
  age = forms.IntegerField()
  dob = forms.DateField()
  
class StudentModelForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = "__all__"