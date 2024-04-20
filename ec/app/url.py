from django.urls import path
from . import views

# In this file we add all URLs related to the app (APP URL File)
# Then include all in main URL
# Hamid
urlpatterns = [
    path("", views.Home),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
]