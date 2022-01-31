from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.shop, name='shop'),
   path('category/<int:id_category>/', mainapp.shop, name='category'),
   path('detail/<int:pk>/', mainapp.detail, name='detail'),
    ]