from django.shortcuts import render

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
