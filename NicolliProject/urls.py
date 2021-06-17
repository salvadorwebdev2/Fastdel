from django.conf.urls import url, include
from django.contrib import admin
from PresList import views 

urlpatterns = [    
    url(r'hpage', views.home_page, name='home_page'),    
    #url(r'^PresList/new$', views.new_list, name='new_list'),
    url(r'viewlist/', views.view_list, name='view_list'),   
    url(r'viewthree/', views.view3, name='view3'), 
    url(r'viewfour/', views.view4, name='view4'),
    url(r'viewfive/', views.view5, name='view5'),
    #url(r'^PresList/(\d+)/add_item$', views.add_item, name='add_item'),
    url('admin/', admin.site.urls)]
    

