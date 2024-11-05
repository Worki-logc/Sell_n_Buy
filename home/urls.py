from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('register', views.register, name="registerUser"),
    path('deleteuser', views.deleteUser, name="deleteUser"),
    path('add_product', views.add_product, name='add_product'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('deleteProduct/<int:product_id>/', views.deleteProduct, name='deleteProduct'),
    path('cart/', views.cart_details, name='cart_details'),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove_cartItem/<int:product_id>/", views.remove_cartItem, name="remove_cartItem")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)