from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from .views import register
from .views import product_list, add_product, update_product, delete_product, register
from django.conf.urls.static import static


urlpatterns = [
    path('', views.landing_page, name='landing'),  # Landing page URL pattern
    path('product_list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('register/', register, name='register'),  # Registration URL pattern
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

