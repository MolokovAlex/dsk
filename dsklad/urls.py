from django.contrib import admin
from django.urls import path
from dsklad.views import *
# from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path ('dsklad/', index_dsklad, name='sklad_page'),
    path ('', index_dsklad, name='sklad_page'),
    # path('dsklad/edit_DBC/', editDBC, name='edit_DBC'),
    path('edit_DBC/', editDBC, name='edit_DBC'),
    path('edit_DBU/', editDBU, name='edit_DBU'),
    path('edit_DBGC/', editDBGC, name='edit_DBGC'),
    path('income/', income, name='income'),
    path('expenditure/', expenditure, name='expenditure'),
    path('add_test_data_DBC/', add_test_data_DBC, name='add_test_data_DBC'),
    path('add_test_data_DBU/', add_test_data_DBU, name='add_test_data_DBU'),
    path('add_test_data_DBGC/',add_test_data_DBGC, name='add_test_data_DBGC'),
    path('add_test_data_DBI/',add_test_data_DBI, name='add_test_data_DBI'),
    path('writenewgroup', write_new_group, name='write_new_group')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)