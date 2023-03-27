from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.CompanyListView.as_view(), name="company-list"),
    path("companies/new/", views.CompanyCreateView.as_view(), name="company-create"),
    path(
        "companies/edit/<int:pk>/",
        views.CompanyCreateView.as_view(),
        name="company-edit",
    ),
    path(
        "companies/detail/<int:pk>/",
        views.CompanyDetailView.as_view(),
        name="company-detail",
    ),
    path(
        "companies/update/<int:pk>/",
        views.CompanyUpdateView.as_view(),
        name="company-update",
    ),
]
