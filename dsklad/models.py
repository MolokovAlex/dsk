from django.db import models

# --------------- БД склада компонентов --------------------------
# sql_create_table_DBC = """ CREATE TABLE IF NOT EXISTS DBC (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL CHECK(name !=''), 
#         amount INTEGER NOT NULL DEFAULT 0 CHECK(amount >= 0), 
#         id_unit INTEGER,
#         min_rezerve INTEGER NOT NULL DEFAULT 0 CHECK(amount >= 0),
#         articul_1C TEXT,
#         code_1C TEXT,
#         name_1C TEXT,
#         id_parent INTEGER,
#         id_lvl INTEGER,
#         FOREIGN KEY (id_unit)  REFERENCES DBU (id) ON DELETE RESTRICT,
#         FOREIGN KEY (id_parent)  REFERENCES DBG (id) ON DELETE RESTRICT
#         );
#         """

class DBC(models.Model):
    id_dbc = models.IntegerField(verbose_name='id_rowDBC', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Наименование компонента', max_length=150)
    amount = models.IntegerField(verbose_name='Количество')#, blank=True )#INTEGER NOT NULL DEFAULT 0 CHECK(amount >= 0), 
    # id_unit = models.IntegerField(verbose_name='id_ед.изм.')#, blank=True )# id_unit INTEGER,
    id_unit = models.ForeignKey('DBU', on_delete=models.PROTECT, null=True, verbose_name='ед.изм.')
    min_rezerve = models.IntegerField(verbose_name='Мин.кол.на складе')# min_rezerve INTEGER NOT NULL DEFAULT 0 CHECK(amount >= 0),
    articul_1C = models.CharField(verbose_name='Артикул 1С', max_length=20, blank=True )# articul_1C TEXT,
    code_1C = models.CharField(verbose_name='Код 1С', max_length=20, blank=True )# code_1C TEXT,
    name_1C = models.CharField(verbose_name='Наименование 1С', max_length=150, blank=True )# name_1C TEXT,
    # id_parent = models.IntegerField(verbose_name='id_Родительская группа')# id_parent INTEGER,
    id_parent = models.ForeignKey('DBGC', on_delete=models.PROTECT, null=True, verbose_name='родительская группа')
    id_lvl = models.IntegerField(verbose_name='id_резерв', blank=True )# id_lvl INTEGER,

    def __str__(self) -> str:
        return self.name

# sql_create_table_DBU = """ CREATE TABLE IF NOT EXISTS DBU (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL CHECK(name !='')
#         );
#         """

class DBU(models.Model):
    id_dbu = models.IntegerField(verbose_name='id_rowDBU', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Наименование ед.изм', max_length=30)

    def __str__(self) -> str:
        return self.name

# --------------- БД склада DBGroupComponent --------------------------
# сделать список смежности
# sql_create_table_DBG = """ CREATE TABLE IF NOT EXISTS DBG (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL CHECK(name !=''),
#         id_parent INTEGER
#         );
#         """

class DBGC(models.Model):
    id_dbgc = models.IntegerField(verbose_name='id_rowDBGC', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Наименование группы', max_length=50)
    # id_parent = models.IntegerField(verbose_name='id_Родительская группа', null=True)# id_parent INTEGER,
    id_parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, verbose_name='id_Родительская группа')

    def __str__(self) -> str:
        return self.name

# --------------- БД прихода компонентов (income) -------------
# sql_create_table_DBI = """ CREATE TABLE IF NOT EXISTS DBI (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         date TEXT NOT NULL CHECK(date !=''),
#         id_component INTEGER NOT NULL, 
#         amount INTEGER NOT NULL CHECK(amount > 0), 
#         comments TEXT,
#         FOREIGN KEY (id_component)  REFERENCES DBC (id) ON DELETE RESTRICT
#         );
#         """

class DBI(models.Model):
    id_dbi = models.IntegerField(verbose_name='id_rowDBI', primary_key=True, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата прихода' )
    # id_component = models.IntegerField(verbose_name='id_компонент')#INTEGER NOT NULL, 
    id_component = models.ForeignKey('DBC', on_delete=models.PROTECT, null=True, verbose_name='наименование компонента')
    amount = models.IntegerField(verbose_name='Количество')#         amount INTEGER NOT NULL CHECK(amount > 0), 
    comments = models.CharField(verbose_name='комментарии', max_length=150, blank=True) #         comments TEXT
    



# --------------- БД расхода компонентов (expenditure) -------------
# sql_create_table_DBE = """ CREATE TABLE IF NOT EXISTS DBE (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         date TEXT NOT NULL CHECK(date !=''),
#         id_component INTEGER NOT NULL, 
#         amount INTEGER NOT NULL CHECK(amount > 0), 
#         comments TEXT,
#         FOREIGN KEY (id_component)  REFERENCES DBC (id) ON DELETE RESTRICT
#         );
#         """
class DBE(models.Model):
    id_dbe = models.IntegerField(verbose_name='id_rowDBE', primary_key=True, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата расхода' )
    id_component = models.IntegerField(verbose_name='id_компонент')#INTEGER NOT NULL, 
    amount = models.IntegerField(verbose_name='Количество')#         amount INTEGER NOT NULL CHECK(amount > 0), 
    comments = models.CharField(verbose_name='комментарии', max_length=150, blank=True) #         comments TEXT