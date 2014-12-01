from django import forms
 
from submit.models import Groups
 
 
class UploadFileForm(forms.Form):
     
    class Meta:
        model = Groups
		