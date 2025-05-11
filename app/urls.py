from django.urls import path
from . import views

urlpatterns=[
     path('',views.home_page,name='home_page'),
     path('1',views.home,name='index'),
     path('2',views.download,name='download'),
     path('3',views.pan,name='pan'),
     # path('4',views.diaplay_pan,name='display_pan')

]