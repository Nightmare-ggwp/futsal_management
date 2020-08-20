from django import forms
from ground.models import Ground
class GroundForm(forms.ModelForm):
        class Meta:
               model=Ground
               fields="__all__"
