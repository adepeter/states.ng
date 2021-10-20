import random

from django.urls import reverse_lazy
from django.views.generic import FormView

from ..forms.contact import ContactForm

TEMPLATE_URL = 'pages'


class ContactUsView(FormView):
    form_class = ContactForm
    template_name = f'{TEMPLATE_URL}/contact_us.html'
    success_url = reverse_lazy('statesng:pages:contact:contact_us')

    def form_valid(self, form):
        print({k: v for k, v in form.cleaned_data.items()})
        return super().form_valid(form)

    def form_invalid(self, form):
        print({k: v for k, v in form.cleaned_data.items()})
        return super().form_invalid(form)
