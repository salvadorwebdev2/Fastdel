from django.conf.urls import url, include
from django.contrib import admin
from PresList import views 



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^new_list$', views.new_list, name='new_list'),                      
    url(r'^(\d+)/addsend_id$', views.addsend_id, name='addsend_id'),
    url(r'^(\d+)/view_list$', views.view_list, name='view_list'),

    url(r'^edit/(?P<id>\d+)$', views.edit,name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update,name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete,name='delete'),

    ]

    


'''
urlpatterns = [    
    url(r'hmpage', views.home_page, name='home_page'),    
    #url(r'^PresList/new$', views.new_list, name='new_list'),
    url(r'viewlist/', views.view_list, name='view_list'),   
    url(r'viewthree/', views.view3, name='view3'), 
    url(r'viewfour/', views.view4, name='view4'),
    url(r'viewfive/', views.view5, name='view5'),
    #url(r'^PresList/(\d+)/add_item$', views.add_item, name='add_item'),
    url('admin/', admin.site.urls)]
    
'''
