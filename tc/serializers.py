from rest_framework import serializers
from .models import TransferCertificate


class TransferCertificateSerializer(serializers.ModelSerializer):
    tc_image_url = serializers.SerializerMethodField()

    class Meta:
        model = TransferCertificate
        fields = ['id', 'tc_no', 'student_name', 'tc_image', 'tc_image_url', 'created_date', 'delete_status']

    def get_tc_image_url(self, obj):
        if not obj.tc_image:
            return None
        request = self.context.get('request')
        url = f'/media/tc/{obj.tc_image}'
        if request:
            return request.build_absolute_uri(url)
        return f'http://127.0.0.1:8000{url}'