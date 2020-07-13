from rest_framework import serializers
from .models import Meta_Study_Config, Meta_Study_Table_Config, Meta_Table_List, Meta_Table_Column_List

class Meta_Study_Config_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meta_Study_Config
        fields = ('tims_schema', 'schema_name',  'is_study_enabled', 'study_partition')

class Meta_Study_Table_Config_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meta_Study_Table_Config
        fields = ('table_name', 'merge_sp',  'tims_schema', 'schema_name', 'cdc_date', 'sql_data_extract', 'is_enabled')


class Meta_Table_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meta_Table_List
        fields = ('table_name','merge_sp','is_enabled','is_db_load_enabled')


class Meta_Table_Column_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meta_Table_Column_List
        fields = ('table_name','column_name','sequence_number','data_type')

