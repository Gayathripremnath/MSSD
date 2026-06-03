from django.urls import path
from .views import TransferCertificateListCreateView, TransferCertificateDetailView

urlpatterns = [
    path('', TransferCertificateListCreateView.as_view(), name='tc-list-create'),
    path('<int:pk>/', TransferCertificateDetailView.as_view(), name='tc-detail'),
]