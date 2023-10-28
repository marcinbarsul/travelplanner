from django.contrib import admin
from django.urls import path
from travelplanner import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('create_flight/', views.create_flight, name='create_flight'),
    path('travel_costs/', views.travel_costs, name='travel_costs'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
