from django.urls import path
from . import views


urlpatterns = [
    path('citations/', views.CitationListCreateView.as_view(), name='citation-list.create'),
    path('citations/<int:pk>', views.CitationRetrieveUpdateDestroyView.as_view(), name='citation-detail-view')
]
