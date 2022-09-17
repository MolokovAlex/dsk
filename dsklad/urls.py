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
    path('income/', income, name='income'),
    path('expenditure/', expenditure, name='expenditure')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)