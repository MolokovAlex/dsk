from django.shortcuts import render

def index_specification(request):
    return render(request, 'specification/index_specification.html')

def editDBGS(request):
    return render(request, 'specification/index_specification.html')

def editDBS(request):
    return render(request, 'specification/index_specification.html')

def expenditure_specification(request):
    return render(request, 'specification/index_specification.html')