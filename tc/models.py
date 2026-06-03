from django.db import models


class TransferCertificate(models.Model):
    tc_no = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    tc_image = models.TextField()
    created_date = models.DateTimeField()
    delete_status = models.IntegerField(default=0)

    def __str__(self):
        return self.tc_no

    class Meta:
        db_table = 'transfer_certificates'
        managed = False
        ordering = ['-created_date']


