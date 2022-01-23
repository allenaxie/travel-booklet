from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Sign up
    path('accounts/signup/',views.signup, name='signup'),
    # Profile
    path('accounts/profile/',views.profile, name='profile'),
    path('accounts/profile/create', views.profile_create, name='profile_create'),
    # path('accounts/profile/update', views.profile_update, name='profile_update'),
    # Trips
    path('trips/', views.trips_index, name='trips_index'),
    path('trips/create', views.TripCreate.as_view(), name="trips_create"),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name="trips_update"),
    path('trips_delete/<int:trip_id>/', views.trips_delete, name="trips_delete"),
]