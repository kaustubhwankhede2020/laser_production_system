from django.db import models

# Create your models here.
class Components(models.Model):
    main_id = models.AutoField(primary_key=True)
    component_type = models.CharField(max_length=25)
    component_lk_number = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Daily_update(models.Model):
    main_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=15)
    shift = models.CharField(max_length=5)
    employee_number = models.CharField(max_length=10)
    component_type = models.CharField(max_length=25)
    component_lk_number = models.CharField(max_length=25)
    component_lot_number = models.CharField(max_length=5)
    component_quantity = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
