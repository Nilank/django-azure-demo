from django.db import models

# Create your models here.
class Meta_Study_Config(models.Model):
    tims_schema = models.CharField(max_length=60)
    schema_name = models.CharField(max_length=60)
    is_study_enabled = models.BooleanField(default=True)
    study_partition = models.IntegerField(blank=True)

    def __str__(self):
        return self.tims_schema 

class Meta_Study_Table_Config(models.Model):
    table_name = models.CharField(max_length=60)
    merge_sp = models.CharField(max_length=60)
    tims_schema = models.CharField(max_length=60)
    schema_name = models.CharField(max_length=60)
    cdc_date = models.DateTimeField(null=True, blank=True)
    sql_data_extract = models.TextField()
    is_enabled = models.BooleanField(default=True)    

    def __str__(self):
        return self.table_name


class Meta_Table_List(models.Model):
    table_name = models.CharField(max_length=60)
    merge_sp = models.CharField(max_length=60)
    is_enabled = models.BooleanField(default=True)
    is_db_load_enabled = models.BooleanField(default = True)

    def __str__(self):
        return self.table_name


class Meta_Table_Column_List(models.Model):
    table_name = models.CharField(max_length=60)
    column_name = models.CharField(max_length=100)
    sequence_number = models.IntegerField()
    data_type = models.CharField(max_length=60)

    def __str__(self):
        return self.column_name