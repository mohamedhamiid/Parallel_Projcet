from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,PasswordChangeForm,MySetPasswordForm

# In this file we add all URLs related to the app (APP URL File)
# Then include all in main URL
# Hamid
urlpatterns = [
    path("", views.home),
    # path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    # kiro 
    path('profile/',views.ProfileView.as_view(),name='profile') ,
    #sarsourr
    path('address/',views.AddressView.as_view(),name='address') ,
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress') ,

    #mariam
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name="showcart"),
    path('checkout/', views.checkout.as_view(), name="checkout"),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
    path('pluscart/', views.plus_cart, name="pluscart"),
    path('minuscart/', views.minus_cart, name="minuscart"),
    path('removecart/', views.remove_cart, name="removecart"),

    #Helmy
    path('search/', views.search, name="search"),


    # path('pluswishlist/', views.plus_wishlist),
    # path('minuswishlist/', views.minus_wishlist),


    #Anas
    #Add login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'), #path of registration
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'), #path of login


    #kiro 
    #password change
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=PasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    #Logout 
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    #forget Password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class= MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('test/',views.test,name='test'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
