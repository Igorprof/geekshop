from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'), 
    path('users/', adminapp.admin_users, name='admin_users'),
    path('users/create/', adminapp.admin_users_create, name='admin_users_create'),
    path('users/update/<int:user_id>/', adminapp.admin_users_update, name='admin_users_update'),
    path('users/remove/<int:user_id>/', adminapp.admin_users_remove, name='admin_users_remove'),
    path('product_categories/', adminapp.admin_product_categories, name='admin_product_categories'),
    path('product_categories/update/<int:product_category_id>', adminapp.admin_product_categories_update, name='admin_product_categories_update'),
    path('product_categories/create/', adminapp.admin_product_categories_create, name='admin_product_categories_create'),
    path('product_categories/remove/<int:product_category_id>/', adminapp.admin_product_categories_remove, name='admin_product_categories_remove'),
]