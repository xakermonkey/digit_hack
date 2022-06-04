from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            return redirect("main")
        else:
            return render(request, 'employee/login.html')
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

