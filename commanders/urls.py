from django.urls import path
from . import views

urlpatterns = [
    path('commanders/', views.CommanderListCreateView.as_view(), name='commander-list-create'),
    path('commanders/<int:pk>/', views.CommanderRetrieveUpdateDestroyView.as_view(), name='commander-detail-view')
]
