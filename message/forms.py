from django import forms
#from captcha.fields import ReCaptchaField
from .models import Ordering

class OrderingForm(forms.ModelForm):

    class Meta:
        model = Ordering
        fields = ('author', 'email', 'title', 'message', 'age', 'eye_color', 'rice', 'boobs', 'waist', 'hair_color', 'taz', 'foot')
