from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FruitipediaApp.fruit_app.urls')),
    path('profile/', include('FruitipediaApp.profile_app.urls')),
]
