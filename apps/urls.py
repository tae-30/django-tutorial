from django.urls import include, path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

# app_name = "apps"
urlpatterns = [
    path("", views.index, name="index"),
] + debug_toolbar_urls()
