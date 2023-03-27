from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from . import models


class CompanyListView(ListView):
    model = models.Company


class CompanyDetailView(DetailView):
    model = models.Company


class ValidateMixin:
    def form_valid(self, form):
        if form.is_valid() and not self.request.up.validate:
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))


class CompanyCreateView(ValidateMixin, CreateView):
    model = models.Company
    fields = ["name", "address"]


class CompanyUpdateView(ValidateMixin, UpdateView):
    model = models.Company
    fields = ["name", "address"]
