from django.urls import path
from order import views

urlpatterns = [
    path('shop/', views.shop, name="shop"),
    path('menu/<int:shop>', views.menu, name="menu"),
]