from django.contrib import admin
from django.urls import path
from specification.views import *
# from django.urls import include

urlpatterns = [
    path ('', index_specification, name='specification_page'),
    path('editDBGS/', editDBGS, name='edit_DBGS'),
    path('editDBS/', editDBS, name='edit_DBS'),
    path('expenditure_specification/', expenditure_specification, name='expenditure_specification')

]