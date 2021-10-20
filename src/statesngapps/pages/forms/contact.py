import random

from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_random = random.randint(1, 10)
        second_random = random.randint(1, 3)
        self.fields['captcha'].label = f'{first_random} + {second_random}'
        self.fields['first_random'].initial = first_random
        self.fields['second_random'].initial = second_random

    def clean(self):
        cleaned_data = super().clean()
        if self.cleaned_data.get('captcha') != self.cleaned_data.get('first_random') + \
                self.cleaned_data.get('second_random'):
            self.add_error('captcha', _('Incorrect captcha'))
        return cleaned_data

    # title = forms.CharField()
    # firstname = forms.CharField()
    # lastname = forms.CharField()
    # email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea)
    first_random = forms.IntegerField(widget=forms.HiddenInput)
    second_random = forms.IntegerField(widget=forms.HiddenInput)
    captcha = forms.IntegerField(widget=forms.TextInput)
