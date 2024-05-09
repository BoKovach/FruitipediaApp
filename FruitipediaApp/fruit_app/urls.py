from django.urls import path

from FruitipediaApp.fruit_app import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create fruit'),
    path('<int:pk>/details/', views.fruit_details, name='fruit details'),
    path('<int:pk>/edit/', views.edit_fruit, name='edit fruit'),
    path('<int:pk>/delete/', views.delete_fruit, name='delete fruit'),
)
