from django import forms
from .models import Aadhar

class AadharForm(forms.ModelForm):
     class Meta:
          model=Aadhar
          fields=['first_name','last_name','father_name','mother_name','DOB','address','state','pin_code','phone','email','aadhar_number','gender','photo']
          # fields='__all__'
