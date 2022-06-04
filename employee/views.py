from django.shortcuts import render


def login(request):
    return render(request, 'employee/login.html')

def recoverpw(request):
    return render(request, 'employee/recoverpw.html')

def main(request):
    return render(request, 'employee/main.html')

def code_to_text(request):
    return render(request, 'employee/code_to_text.html')

def products(request):
    return render(request, 'employee/products.html')

def products_details(request):
    return render(request, 'employee/products_details.html')

def documentation(request):
    return render(request, 'employee/documentation.html')

