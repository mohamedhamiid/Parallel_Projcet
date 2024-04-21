from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# In this file we add all URLs related to the app (APP URL File)
# Then include all in main URL
# Hamid
urlpatterns = [
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
]+static(settings.MEDIA_URL, dociment_root=settings.MEDIA_ROOT)