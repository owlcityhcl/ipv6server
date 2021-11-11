from django import forms
from django.utils.timezone import now
from .models import UploadedImageModel
 
class UploadedImageForm(forms.ModelForm):
 
   class Meta:
       model = UploadedImageModel
       #fields = '__all__'
       fields = ['id_card','own_name','pic_type']
