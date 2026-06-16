import os
from django.core.exceptions import ValidationError
from django.db import models

def validate_image(file):
    ext = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png']

    if ext not in valid_extensions:
        raise ValidationError("Only JPG and PNG files are allowed!")


class TransferCertificate(models.Model):
    tc_no = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    tc_image = models.ImageField(upload_to='tc/', validators=[validate_image])
    created_date = models.DateTimeField(auto_now_add=True)
    delete_status = models.IntegerField(default=0)

    class Meta:
        db_table = 'transfer_certificates'

    def __str__(self):
        return self.student_name
