from django.shortcuts import render


def login(request):
    return render(request, 'employee/login.html')

def recoverpw(request):
    return render(request, 'employee/recoverpw.html')

def main(request):
    return render(request, 'employee/main.html')

def employees(request):
    return render(request, 'employee/employees.html')

def products(request):
    return render(request, 'employee/products.html')

def nomenclature(request):
    return render(request, 'employee/nomenclature.html')

