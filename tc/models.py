from django.db import models

class TransferCertificate(models.Model):
    tc_no = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    tc_image = models.ImageField(upload_to='tc/')

    def __str__(self):
        return f"{self.student_name} - {self.tc_no}"

    class Meta:
        db_table = 'transfer_certificates'