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
    path(
        "companies/delete/<int:pk>/",
        views.CompanyDeleteView.as_view(),
        name="company-delete",
    ),
    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path(
        "projects/suggest_name/",
        views.ProjectSuggestNameView.as_view(),
        name="project-suggest-name",
    ),
    path("projects/new/", views.ProjectCreateView.as_view(), name="project-create"),
    path(
        "projects/detail/<int:pk>/",
        views.ProjectDetailView.as_view(),
        name="project-detail",
    ),
    path(
        "projects/update/<int:pk>/",
        views.ProjectUpdateView.as_view(),
        name="project-update",
    ),
    path(
        "projects/delete/<int:pk>/",
        views.ProjectDeleteView.as_view(),
        name="project-delete",
    ),
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    path("tasks/clear/", views.ClearTasksView.as_view(), name="task-clear"),
    path("tasks/new/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/detail/<int:pk>/",
        views.TaskDetailView.as_view(),
        name="task-detail",
    ),
    path(
        "tasks/update/<int:pk>/",
        views.TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/done/<int:pk>/",
        views.TaskDoneView.as_view(),
        name="task-done",
    ),
]
