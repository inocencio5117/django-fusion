from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, Employee
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()
        return context

    def form_valid(self, form: Any) -> HttpResponse:
        form.send_mail()
        messages.success(self.request, 'E-mail sent succesfully')
        return super().form_valid(form)

    def form_invalid(self, form: Any) -> HttpResponse:
        messages.error(self.request, 'Error on sending e-mail')
        return super().form_invalid(form)