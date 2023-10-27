from django.contrib import admin
from django.urls import path
from travelplanner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_flight/', views.create_flight, name='create_flight'),  # Trasa do widoku tworzenia lotu
    path('travel_costs/', views.travel_costs, name='travel_costs'),
]
