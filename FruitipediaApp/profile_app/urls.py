from django.urls import path

from FruitipediaApp.profile_app import views

urlpatterns = (
    path('create/', views.create_profile, name='create profile'),
    path('details/', views.profile_details, name='profile details'),
    path('edit/', views.edit_profile, name='edit profile'),
    path('delete/', views.delete_profile, name='delete profile'),
)
