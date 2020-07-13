from django.conf.urls import include, url
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/studies/$', views.study_list),
    url(r'^api/studies/(?P<pk>[0-9]+)$', views.study_detail),
    url(r'^api/studies/tables$', views.study_table_list),
    url(r'^api/studies/tables/(?P<pk>[0-9]+)$', views.study_table_detail),
    url(r'^api/tables/list$', views.tables_list),
    url(r'^api/tables/list/(?P<pk>[0-9]+)$', views.tables_list_detail),
    url(r'^api/tables/columns$', views.table_column_list),
    url(r'^api/tables/columns/(?P<pk>[0-9]+)$', views.table_column_detail),
]