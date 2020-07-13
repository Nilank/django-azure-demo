from django.contrib import admin
from .models import Meta_Study_Config, Meta_Study_Table_Config, Meta_Table_List, Meta_Table_Column_List



# Register your models here.
admin.site.register([Meta_Study_Config, Meta_Study_Table_Config, Meta_Table_List, Meta_Table_Column_List])