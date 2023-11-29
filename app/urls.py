
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from app import views 
from django.contrib.auth import views as auth_view

from app.forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm

urlpatterns = [
    path("",views.home),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path("profile/",views.ProfileView.as_view(),name='profile'),
    path("address/",views.address,name='address'),
    path('updateAddress/<int:pk>',views.UpdateAddress.as_view(),name='updateAddress'),

    #login
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    # path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html',name='passwordchangedone')),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'), name='passwordchange'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)