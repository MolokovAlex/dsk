# from asyncio.windows_events import NULL
from asyncio.windows_events import NULL
from calendar import c
from django.shortcuts import render
from .forms import *
from .models import DBC, DBU, DBGC, DBI

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
    dbcAll = DBC.objects.all()
    data_in_template_editDBC= {
        'dbcAll': dbcAll,
        'title': 'Список компонентов',
    }
    return render(request, 'dsklad\editDBC.html', data_in_template_editDBC)

def editDBU(request):
    dbcAll = DBU.objects.all()
    data_in_template_editDBU= {
        'dbcAll': dbcAll,
        'title': 'Список ед.измерения',
    }
    return render(request, 'dsklad\editDBU.html', data_in_template_editDBU)

def editDBGC(request):
    list_dbgcAll = []
    dbgcAll = DBGC.objects.all()
    for item in dbgcAll:
        di = {}
        di['id'] = item.id_dbgc
        di['name'] = item.name
        di['parent'] = item.id_parent
        di['path'] = createPathParent(item=item, db=dbgcAll)
        list_dbgcAll.append(di)
    data_in_template_editDBGC= {
        'list_dbgcAll': list_dbgcAll,
        'title': 'Список групп компонентов',
    }
    return render(request, 'dsklad\editDBGC.html', data_in_template_editDBGC)

def createPathParent(item, db):
    path = ''
    if item.id_parent:
        a = str(item.id_parent)
        while a != 'None':
            path = a+'\\'+path
            for item2 in db:
                b = str(item2.name)
                if a == b:
                    a = str(item2.id_parent)
                    break
    return path

def income(request):
    incomeAll = DBI.objects.all()
    DBCAll = DBC.objects.all()
    # dsfgf = DBC.id_parent
    data_in_template_income= {
        'incomeAll': incomeAll,
        'DBC_all':DBCAll,
        'title': 'Список приходов',
    }
    return render(request, 'dsklad\income.html', context=data_in_template_income)

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
        field_DBC = ['name','amount','id_unit_id','min_rezerve','articul_1C','code_1C','name_1C','id_parent_id','id_lvl']
        for item in data_list_demo_DBC:
            row_data_in_DBC = {field_DBC:item for (field_DBC,item) in zip(field_DBC,item)}
            DBC.objects.create(**row_data_in_DBC)  
    else:       #  GET получаем форму на монитор
        pass
    return render(request, 'dsklad\dd_test_data_DBC.html')

def add_test_data_DBI(request):
    data_list_demo_DBI = [
        ('1999-12-01 22:01:15', 1,  1,  'из ЧипиДипа счет 2345 от 1999-11-01'),        #id=1
        ('1999-12-02 08:07:15', 2,  2,  'из ЧипиДипа счет 2345 от 1999-11-01'),        #id=2
        ('1999-12-03 09:04:15', 3,  1,  'из ЧипиДипа счет 2345 от 1999-11-01'),        #id=3
    ]
    if request.method == 'POST': # отправляем данные с формы с монитора
        field_DBI = ['date', 'id_component', 'amount', 'comments']
        for item in data_list_demo_DBI:
            row_data_in_DBI = {field_DBI:item for (field_DBI,item) in zip(field_DBI,item)}
            DBI.objects.create(**row_data_in_DBI)  
    else:       #  GET получаем форму на монитор
        pass
    return render(request, 'dsklad\dd_test_data_DBI.html')

def add_test_data_DBU(request):
    data_list_demo_DBU = [
        ('шт',),                #id=1             
        ('мл',),                #id=2 
        ('л',),                 #id=3 
        ('мм',),                #id=4 
        ('см',),                #id=5 
        ('м',),                 #id=6 
        ('км',),                #id=7 
        ('г',),                 #id=8 
        ('кг',),                #id=9 
        ('т',),                 #id=10 
        ('компл',)              #id=11 
    ]
    if request.method == 'POST': # отправляем данные с формы с монитора
        field_DBU = ['name']
        for item in data_list_demo_DBU:
            row_data_in_DBU = {field_DBU:item for (field_DBU,item) in zip(field_DBU,item)}
            DBU.objects.create(**row_data_in_DBU)  
    else:       #  GET получаем форму на монитор
        pass
    return render(request, 'dsklad\dd_test_data_DBU.html')

def add_test_data_DBGC(request):
    # data_list_demo_DBGC = [
    #     ('Склад',       1),     #id=1
    #     ('Разъемы',     1),     #id=2
    #     ('DIN',         2),     #id=3
    #     ('СП Каскад',   2),     #id=4
    #     ('6Р100-6Р150', 2),     #id=5
    #     ('СНП407-100',  4),     #id=6
    #     ('СНП407-150',  4),     #id=7
    #     ('6Р100',       5),     #id=8
    #     ('6Р150',       5),     #id=9
    #     ('DIN 32 конт', 3),     #id=10
    #     ('DIN 64 конт', 3),     #id=11
    #     ('Микросхемы',  1),     #id=12
    #     ('Аналоговые',  12),    #id=13
    #     ('Цифровые',    12),    #id=14
    #     ('прочие',      12)     #id=15
    #     ]
    data_list_demo_DBGC = [
        ('Склад',       ),     #id=1
        ('Разъемы',     ),     #id=2
        ('DIN',         ),     #id=3
        ('СП Каскад',   ),     #id=4
        ('6Р100-6Р150', ),     #id=5
        ('СНП407-100',  ),     #id=6
        ('СНП407-150',  ),     #id=7
        ('6Р100',       ),     #id=8
        ('6Р150',       ),     #id=9
        ('DIN 32 конт', ),     #id=10
        ('DIN 64 конт', ),     #id=11
        ('Микросхемы',  ),     #id=12
        ('Аналоговые',  ),    #id=13
        ('Цифровые',    ),    #id=14
        ('прочие',      )     #id=15
        ]
    if request.method == 'POST': # отправляем данные с формы с монитора
        field_DBGC = ['name', 'id_parent']
        for item in data_list_demo_DBGC:
            row_data_in_DBGC = {field_DBGC:item for (field_DBGC,item) in zip(field_DBGC,item)}
            DBGC.objects.create(**row_data_in_DBGC)  
    else:       #  GET получаем форму на монитор
        pass
    return render(request, 'dsklad\dd_test_data_DBGC.html')  

def write_new_group(request) :
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'dsklad\editDBGC.html') 