from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('add_institute_info/',views.add_institute_info,name='add_institute_info'),
    path('add_cycle_info/',views.add_cycle_info,name='add_cycle_info'),
    path('show_cycle_info/<str:year>/<str:semester>/', views.show_cycle_info, name='show'),
    path('event',views.all_event,name='all')
   
]
