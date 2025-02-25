from django.urls import path
from . import views


urlpatterns = [
    path('battles/', views.BattleListCreateView.as_view(), name='battle-list-create'),
    path('battles/<int:pk>/', views.BattleRetrieveUpdateDestroyView.as_view(), name='battle-detail-view')
]
