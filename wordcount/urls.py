
from django.urls import path
from . import views
from . import views2
urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
    # path('dsddd/',views.get,name='455')
    path("fig/",views2.home22,name= "home2"),
    path("fig/fig2/",views2.cc,name = "count2"),
    path("fig/fig3/",views2.gg,name = "aboout")


]
