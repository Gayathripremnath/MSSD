from rest_framework import serializers
from .models import TransferCertificate


class TransferCertificateSerializer(serializers.ModelSerializer):
    tc_image_url = serializers.SerializerMethodField()

    class Meta:
        model = TransferCertificate
        fields = [
            'id',
            'tc_no',
            'student_name',
            'tc_image',
            'tc_image_url',
            'created_date',
            'delete_status'
        ]

    def get_tc_image_url(self, obj):
        if not obj.tc_image:
            return None

        request = self.context.get('request')

        # BEST PRACTICE (Django handles path correctly)
        if request:
            return request.build_absolute_uri(obj.tc_image.url)

        return obj.tc_image.url