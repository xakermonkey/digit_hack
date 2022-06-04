from django.shortcuts import render


def login(request):
    return render(request, 'definition_system/login.html')

def recoverpw(request):
    return render(request, 'definition_system/recoverpw.html')

def main(request):
    return render(request, 'definition_system/main.html')

def employees(request):
    return render(request, 'definition_system/employees.html')

def products(request):
    return render(request, 'definition_system/products.html')

def nomenclature(request):
    return render(request, 'definition_system/nomenclature.html')

