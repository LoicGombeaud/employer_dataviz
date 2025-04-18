from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("employers/", include("employers.urls")),
    path("territories/", include("territories.urls")),
    path("admin/", admin.site.urls),
    path(
        "accounts/login/",
        LoginView.as_view(
            template_name="admin/login.html",
            extra_context={
                "title": "Login",
                "site_title": "Employer Dataviz",
                "site_header": "Employer Dataviz",
            }),
            name="login"),
]
