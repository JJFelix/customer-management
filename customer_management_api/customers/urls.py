from django.urls import path
from . import views

urlpatterns = [
    # oauth
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path("is_logged_in", views.is_logged_in, name="is_logged_in"),
    path("test", views.test, name="test"),


    # customers
    path("customers", views.get_customers, name="get_customers"),
    path("customers/<str:customer_id>", views.get_customer, name="get_customer"),
    path('customers/add/', views.add_customer, name="add_customer"),
    path('customers/update/<str:customer_id>', views.update_customer, name="update_customer"),
    path('customers/delete/<str:customer_id>', views.delete_customer, name="delete_customer"),

    # orders
    path("orders", views.get_orders, name="get_orders"),
    path('orders/add', views.add_order, name="add_order"),
    path('orders/update/<str:order_id>', views.update_order, name="update_order"),
    path('orders/delete/<str:order_id>', views.delete_order, name="delete_order"),
]