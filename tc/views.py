from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import TransferCertificate
from .serializers import TransferCertificateSerializer


class TransferCertificateListCreateView(generics.ListCreateAPIView):
    queryset = TransferCertificate.objects.filter(delete_status=0)
    serializer_class = TransferCertificateSerializer
    parser_classes = [MultiPartParser, FormParser]


class TransferCertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransferCertificate.objects.all()
    serializer_class = TransferCertificateSerializer
    parser_classes = [MultiPartParser, FormParser]