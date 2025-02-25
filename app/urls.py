from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('factions.urls')),
    path('api/v1/', include('commanders.urls')),
    path('api/v1/', include('wars.urls')),
    path('api/v1/', include('battles.urls')),
    path('api/v1/', include('citations.urls'))
]
