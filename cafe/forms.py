from django import forms
from cafe.models import Cafe
class CafeForm(forms.ModelForm):
        class Meta:
               model=Cafe
               fields="__all__"
