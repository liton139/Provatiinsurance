from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data = [

        ("provatiadmin", "provatiadmin"),
        ("provati_itdept","provati_itdept"),
        ('emp',"emp")
    ]
    depertment = [
        ('Admin_depertment',"Admin_depertment"),
        ('it_depertment',"it_depertment"),
        ('clams_deprtment',"clams_deprtment"),
        ('mds_deprtment',"mds_deprtment"),
        ('uw_deprtment',"uw_deprtment")
    ]
    ho_branch = [
        ('ho',"ho"),
        ('branch',"branch"),
    ]

    user_type = models.CharField(default='provati_itdept',choices=user_type_data,max_length=100)
    title = models.CharField(max_length=100)
    dept = models.CharField(max_length=100,choices=depertment)
    ho_br = models.CharField(max_length=100,choices=ho_branch)
    mobile = models.CharField(max_length=11)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#
#
#
#
# class provati_pc_info(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     rank = models.CharField(max_length=255)
#     dept = models.CharField(max_length=255)
#     provati_ho_br = models.CharField(max_length=255)
#     pctype = models.CharField(max_length=255)
#     pcbrand = models.CharField(max_length=255)
#     pcbrandserial = models.CharField(max_length=255)
#     mainboard_brand = models.CharField(max_length=255)
#     mainboard_serial = models.CharField(max_length=255)
#     process_type = models.CharField(max_length=255)
#     process_serial = models.CharField(max_length=255)
#     ram_brand = models.CharField(max_length=255)
#     ram_type = models.CharField(max_length=255)
#     ram_serial = models.CharField(max_length=255)
#     ram_size = models.CharField(max_length=255)
#     harddisk_brand = models.CharField(max_length=255)
#     harddisk_type = models.CharField(max_length=255)
#     harddisk_serial = models.CharField(max_length=255)
#     dvd_brand = models.CharField(max_length=255)
#     dvd_serial = models.CharField(max_length=255)
#     deliverydate = models.DateField(auto_now_add=True)
#     bill_no = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     object = models.Manager()
#
# class provati_monitor_info(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     rank = models.CharField(max_length=255)
#     dept = models.CharField(max_length=255)
#     provati_ho_br = models.CharField(max_length=255)
#     monitor_brand = models.CharField(max_length=255)
#     monitor_serial = models.CharField(max_length=255)
#     deliverydate = models.DateField(auto_now_add=True)
#     bill_no = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     object = models.Manager()
#
#
# class provati_printer_info(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     dept = models.CharField(max_length=255)
#     provati_ho_br = models.CharField(max_length=255)
#     printer_brand = models.CharField(max_length=255)
#     printer_serial = models.CharField(max_length=255)
#     deliverydate = models.DateField(auto_now_add=True)
#     bill_no = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     object = models.Manager()
#
# class provati_ups_info(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     dept = models.CharField(max_length=255)
#     provati_ho_br = models.CharField(max_length=255)
#     ups_brand = models.CharField(max_length=255)
#     ups_serial = models.CharField(max_length=255)
#     deliverydate = models.DateField(auto_now_add=True)
#     bill_no = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     object = models.Manager()
#
# class provati_tech_service(models.Model):
#     id = models.AutoField(primary_key=255)
#     request_from = models.CharField(max_length=255)
#     request_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     submit_by = models.CharField(max_length=255)
#     submit_date = models.DateTimeField(auto_now_add=True)
#     object = models.Manager()
#
# class provati_other_service(models.Model):
#     id = models.AutoField(primary_key=255)
#     solve_com = models.CharField(max_length=255)
#     bill_no = models.CharField(max_length=255)
#     provati_ho_br = models.CharField(max_length=255)
#     request_from = models.CharField(max_length=255)
#     request_by = models.CharField(max_length=255)
#     submit_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     object = models.Manager()


