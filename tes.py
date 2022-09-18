data_list_demo_DBC = [
        ('К155ЛА3', 15,     1,  10, 'К155ЛА3',  '00101217551',  'nК155ЛА3', 14,  0),            #id=1
        ('К155ЛА4', 5,      1,  10, 'К155ЛА4',  '00101217552',  'nК155ЛА4', 14,  0),            #id=2
        ('К155ЛА8', 6,      1,  1,  'К155ЛА8',  '00101217553',  'nК155ЛА8', 14,  0),            #id=3
        ('6Р100 вилка кабельная', 6,      1,  1,  'К155ЛА8',  '00101217553',  'nК155ЛА8', 8,  0),            #id=4
        ('6Р150 розетка блочная', 6,      1,  1,  'К155ЛА8',  '00101217553',  'nК155ЛА8', 9,  0)            #id=5
]
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
field_DBC = ('name','amount','id_unit','min_rezerve','articul_1C','code_1C','name_1C','id_parent','id_lvl')
for item in data_list_demo_DBC:
            row = {field_DBC:item for (field_DBC,item) in zip(field_DBC,item)}
        #     print (row)

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
field_DBU = ['name']
for item in data_list_demo_DBU:
            row_data_in_DBU = {field_DBU:item for (field_DBU,item) in zip(field_DBU,item)}
 

data_list_demo_DBGC = [
        ('Склад',       0),     #id=1
        ('Разъемы',     1),     #id=2
        ('DIN',         2),     #id=3
        ('СП Каскад',   2),     #id=4
        ('6Р100-6Р150', 2),     #id=5
        ('СНП407-100',  4),     #id=6
        ('СНП407-150',  4),     #id=7
        ('6Р100',       5),     #id=8
        ('6Р150',       5),     #id=9
        ('DIN 32 конт', 3),     #id=10
        ('DIN 64 конт', 3),     #id=11
        ('Микросхемы',  1),     #id=12
        ('Аналоговые',  12),    #id=13
        ('Цифровые',    12),    #id=14
        ('прочие',      12)     #id=15
        ]
field_DBGC = ['name', 'id_parent']
for item in data_list_demo_DBGC:
            row_data_in_DBGC = {field_DBGC:item for (field_DBGC,item) in zip(field_DBGC,item)}          