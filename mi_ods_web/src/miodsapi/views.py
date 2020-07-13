from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import Meta_Study_Config_Serializer, Meta_Study_Table_Config_Serializer, Meta_Table_List_Serializer, Meta_Table_Column_List_Serializer

from .models import Meta_Study_Config, Meta_Study_Table_Config, Meta_Table_List, Meta_Table_Column_List

@api_view(['GET', 'POST', 'DELETE'])
def study_list(request):
    if request.method == 'GET':
        studies = Meta_Study_Config.objects.all()

        schema_name = request.query_params.get('schema_name', None)
        if schema_name is not None:
            studies = studies.filter(title__icontains=schema_name)
        
        studies_serializer = Meta_Study_Config_Serializer(studies, many=True)
        return JsonResponse(studies_serializer.data, safe=False)

    elif request.method == 'POST':
        studies_data = JSONParser().parse(request)
        studies_serializer = Meta_Study_Config_Serializer(data=studies_data)
        if studies_serializer.is_valid():
            studies_serializer.save()
            return JsonResponse(studies_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(studies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Meta_Study_Config.objects.all().delete()
        return JsonResponse({'message':'{} Studies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def study_detail(request, pk):
    try:
        study = Meta_Study_Config.objects.get(pk=pk)
    except Meta_Study_Config.DoesNotExist:
        return JsonResponse({'message': 'The study does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        studies_serializer = Meta_Study_Config_Serializer(study)
        return JsonResponse(studies_serializer.data)
    
    elif request.method == 'PUT':
        studies_data = JSONParser().parse(request)
        studies_serializer = Meta_Study_Config_Serializer(study, data=studies_data)
        if studies_serializer.is_valid():
            studies_serializer.save()
            return JsonResponse(studies_serializer.data)
        return JsonResponse(studies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        study.delete()
        return JsonResponse({'message': 'Study was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','DELETE'])
def study_table_list(request):
    if request.method == 'GET':
        tables = Meta_Study_Table_Config.objects.all()

        table_name = request.query_params.get('table_name', None)
        if table_name is not None:
            studies = studies.filter(title__icontains=table_name)
        
        tables_serializer = Meta_Study_Table_Config_Serializer(tables, many=True)
        return JsonResponse(tables_serializer.data, safe=False)

    elif request.method == 'POST':
        tables_data = JSONParser().parse(request)
        tables_serializer = Meta_Study_Table_Config_Serializer(data=tables_data)
        if tables_serializer.is_valid():
            tables_serializer.save()
            return JsonResponse(tables_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tables_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Meta_Study_Table_Config.objects.all().delete()
        return JsonResponse({'message':'{} Tables were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def study_table_detail(request,pk):
    try:
        table = Meta_Study_Table_Config.objects.get(pk=pk)
    except Meta_Study_Table_Config.DoesNotExist:
        return JsonResponse({'message': 'The table does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tables_serializer = Meta_Study_Table_Config_Serializer(table)
        return JsonResponse(tables_serializer.data)
    
    elif request.method == 'PUT':
        tables_data = JSONParser().parse(request)
        tables_serializer = Meta_Study_Table_Config_Serializer(table, data=tables_data)
        if tables_serializer.is_valid():
            tables_serializer.save()
            return JsonResponse(tables_serializer.data)
        return JsonResponse(tables_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        table.delete()
        return JsonResponse({'message': 'Table was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def tables_list(request):
    if request.method == 'GET':
        tables = Meta_Table_List.objects.all()

        table_name = request.query_params.get('table_name', None)
        if table_name is not None:
            studies = studies.filter(title__icontains=table_name)
        
        table_list_serializer = Meta_Table_List_Serializer(tables, many=True)
        return JsonResponse(table_list_serializer.data, safe=False)

    elif request.method == 'POST':
        tables_data = JSONParser().parse(request)
        table_list_serializer = Meta_Table_List_Serializer(data=tables_data)
        if table_list_serializer.is_valid():
            table_list_serializer.save()
            return JsonResponse(table_list_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(table_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Meta_Table_List.objects.all().delete()
        return JsonResponse({'message':'{} Tables were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def tables_list_detail(request,pk):
    try:
        table = Meta_Table_List.objects.get(pk=pk)
    except Meta_Table_List.DoesNotExist:
        return JsonResponse({'message': 'The table does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        tables_serializer = Meta_Table_List_Serializer(table)
        return JsonResponse(tables_serializer.data)
    
    elif request.method == 'PUT':
        tables_data = JSONParser().parse(request)
        tables_serializer = Meta_Table_List_Serializer(table, data=tables_data)
        if tables_serializer.is_valid():
            tables_serializer.save()
            return JsonResponse(tables_serializer.data)
        return JsonResponse(tables_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        table.delete()
        return JsonResponse({'message': 'Table was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def table_column_list(request):
    if request.method == 'GET':
        table_columns = Meta_Table_Column_List.objects.all()

        column_name = request.query_params.get('column_name', None)
        if column_name is not None:
            studies = studies.filter(title__icontains=column_name)
        table_column_list_serializer = Meta_Table_Column_List_Serializer(table_columns, many=True)
        return JsonResponse(table_column_list_serializer.data, safe=False)
        
    elif request.method == 'POST':
        column_data = JSONParser().parse(request)
        table_column_list_serializer = Meta_Table_Column_List_Serializer(data=column_data)
        if table_column_list_serializer.is_valid():
            table_column_list_serializer.save()
            return JsonResponse(table_column_list_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(table_column_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Meta_Table_Column_List.objects.all().delete()
        return JsonResponse({'message':'{} Table columns were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def table_column_detail(request,pk):
    try:
        table_columns = Meta_Table_Column_List.objects.get(pk=pk)
    except Meta_Table_Column_List.DoesNotExist:
        return JsonResponse({'message': 'The table column does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        table_column_serializer = Meta_Table_Column_List_Serializer(table_columns)
        return JsonResponse(table_column_serializer.data)
    
    elif request.method == 'PUT':
        tables_column_data = JSONParser().parse(request)
        table_column_serializer = Meta_Table_Column_List_Serializer(table_columns, data=tables_column_data)
        if table_column_serializer.is_valid():
            table_column_serializer.save()
            return JsonResponse(table_column_serializer.data)
        return JsonResponse(table_column_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        table_columns.delete()
        return JsonResponse({'message': 'Table column was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

