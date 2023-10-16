from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Service, Employee


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()
        return context