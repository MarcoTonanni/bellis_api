from django.urls import path
from . import views


urlpatterns = [
    path('factions/', views.FactionListCreateView.as_view(), name='faction-list-create'),
    path('factions/<int:pk>/', views.FactionRetrieveUpdateDestroyView.as_view(), name='faction-detail-view'),
    path('factions/stats/', views.FactionStatsView.as_view(), name='faction-stats-view')
]
