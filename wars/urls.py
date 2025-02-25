from django.urls import path
from . import views


urlpatterns = [
    path('wars/', views.WarListCreateView.as_view(), name='war-list-create'),
    path('wars/<int:pk>/', views.WarRetrieveUpdateDestroyView.as_view(), name='war-detail-view'),
    path('wars/stats/', views.WarStatsView.as_view(), name='war-stats-view')
]
