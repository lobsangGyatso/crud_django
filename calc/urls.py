from django.urls import path
from . import views 

urlpatterns = [
    # path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('detail',views.detail,name='detail'),
    path('',views.add_show,name='add_show'),
    path('delete_data/<int:id>',views.delete_data,name='deletedata'),
    path('update_data/<int:id>',views.update_data,name="updatedata")
]