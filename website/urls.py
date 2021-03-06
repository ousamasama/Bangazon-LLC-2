from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),

    # Products -----------
    path('search_results/', views.search_results, name='search_results'),
    path('product_sell/', views.product_sell, name='product_sell'),
    path('product_cat/', views.product_cat, name='product_cat'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_books', views.product_books, name='product_books'),
    path('product_furniture', views.product_furniture, name='product_furniture'),
    path('product_misc', views.product_misc, name='product_misc'),
    path('product_jewelry', views.product_jewelry, name='product_jewelry'),
    path('product_cars', views.product_cars, name='product_cars'),
    path('product_electronics', views.product_electronics, name='product_electronics'),
    path('product_computers', views.product_computers, name='product_computers'),
    # End Products -----------


    # Order --------------
    path('order_product/<int:product_id>', views.order_product, name='order_product'),
    path('order_detail/<int:order_id>', views.order_detail, name='order_detail'),
    path('order_payment/<int:order_id>', views.order_payment, name='order_payment'),
    path('order_cancel/<int:order_id>', views.order_cancel, name='order_cancel'),
    path('order_product_to_delete/<int:order_product_to_delete>', views.order_product_to_delete, name='order_product_to_delete'),
    path('order_success/<int:order_id>', views.order_success, name='order_success'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    # End Order --------------

    # My Account ---------
    path('my_account/<int:user_id>/', views.my_account, name='my_account'),
    path('my_account/payment/<int:user_id>/', views.my_account_payment, name='my_account_payment'),
    path('my_account/payment/add/<int:user_id>/', views.my_account_payment_add, name='my_account_payment_add'),
    path('my_account/payment/delete/<int:payment_type_id>',views.my_account_payment_delete, name='my_account_payment_delete'),
    path('my_account/orders/<int:user_id>/', views.my_account_order_history, name='my_account_order_history'),
    path('my_account/orders/detail/<int:order_id>/', views.my_account_order_detail, name='my_account_order_detail')
    # End My Account ---------





    # order
    # product_detail/<int:product_id>/
    # order_payment
    # order_success
    # search_results
    # my_account_payment
    # my_account_order_history
    # my_account_order_detail - my_account/order_detail<int:product_id>/
]