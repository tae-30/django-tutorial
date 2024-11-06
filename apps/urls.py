from django.urls import include, path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

# app_name = "apps"
urlpatterns = [
    path("index", views.index, name="index"),
    path("schedule/", views.schedule, name="schedule"),
] + debug_toolbar_urls()
