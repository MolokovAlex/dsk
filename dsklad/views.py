from django.shortcuts import render
from .forms import *
from .models import DBC

def index(request):
    data_in_template_Index = {
        # 'catalogObjectsAll': catalog_objects_all , 
        'title': 'Сайт ПО',
        # 'sellers': sellers,
        }
    return render(request, 'index.html', context=data_in_template_Index)

def index_dsklad(request):
    return render(request, 'dsklad\index_dsklad.html')

def editDBC(request):
    return render(request, 'dsklad\editDBC.html')

def income(request):
    return render(request, 'dsklad\income.html')

def expenditure(request):
    return render(request, 'dsklad\expenditure.html')


def add_test_data_DBC(request):
    data_list_demo_DBC = [
        ('К155ЛА3', 15,     1,  10, 'К155ЛА3',  '00101217551',  'nК155ЛА3', 14,  0),            #id=1
        ('К155ЛА4', 5,      1,  10, 'К155ЛА4',  '00101217552',  'nК155ЛА4', 14,  0),            #id=2
        ('К155ЛА8', 6,      1,  1,  'К155ЛА8',  '00101217553',  'nК155ЛА8', 14,  0),            #id=3
        ('6Р100 вилка кабельная', 6,      1,  1,  'К155ЛА8',  '00101217553',  'nК155ЛА8', 8,  0),            #id=4
        ('6Р150 розетка блочная', 6,      1,  1,  'К155ЛА8',  '00101217553',  'nК155ЛА8', 9,  0)            #id=5
    ]
    if request.method == 'POST': # отправляем данные с формы с монитора
        row_data_in_DBC = {
            # 'id_dbc': = models.IntegerField(verbose_name='id_rowDBC', primary_key=True, unique=True)
            'name': 'К155ЛА3',
            'amount': 15, 
            'id_unit': 1,
            'min_rezerve': 10,
            'articul_1C': 'К155ЛА3',
            'code_1C': '00101217551',
            'name_1C': 'nК155ЛА3',
            'id_parent': 14,
            'id_lvl': 0
        }
        field_DBC = ['name','amount','id_unit','min_rezerve','articul_1C','code_1C','name_1C','id_parent','id_lvl']
        # for item in data_list_demo_DBC:

        DBC.objects.create(**row_data_in_DBC)  
        pass
    else:       #  GET получаем форму на монитор
        pass

    return render(request, 'dsklad\dd_test_data_DBC.html')

    id_dbc = models.IntegerField(verbose_name='id_rowDBC', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Наименование компонента', max_length=150)
    amount = models.IntegerField(verbose_name='Количество')#, blank=True )#INTEGER NOT NULL DEFAULT 0 CHECK(amount >= 0), 
    id_unit = models.IntegerField(verbose_name='id_ед.изм.')#, blank=True )# id_unit INTEGER,
    min_rezerve = models.IntegerField(verbose_name='Мин.кол.на складе')# min_rezerve INTEGER NOT NULL DEFAULT 0 CHECK(amount >= 0),
    articul_1C = models.CharField(verbose_name='Артикул 1С', max_length=20, blank=True )# articul_1C TEXT,
    code_1C = models.CharField(verbose_name='Код 1С', max_length=20, blank=True )# code_1C TEXT,
    name_1C = models.CharField(verbose_name='Наименование 1С', max_length=150, blank=True )# name_1C TEXT,
    id_parent = models.IntegerField(verbose_name='id_Родительская группа')# id_parent INTEGER,
    id_lvl = models.IntegerField(verbose_name='id_резерв', blank=True )# id_lvl INTEGER,