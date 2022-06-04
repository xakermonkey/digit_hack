from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
import json
from .models import *
import model


def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            return redirect("main")
        else:
            return render(request, 'employee/login.html')
    return render(request, 'employee/login.html')

def recoverpw(request):
    return render(request, 'employee/recoverpw.html')


def create_object(data):
    if len(data["code"]) == 4:
        ProductPosition.objects.create(name=data["name"], code=data["code"])
    elif len(data["code"]) == 6:
        SubPosition.objects.create(name=data["name"], code=data["code"])
    elif len(data["code"]) == 8:
        UnderSubPosition.objects.create(name=data["name"], code=data["code"])


def add_db(data):
    if not "sub_group" in data.keys() and len(data["code"]) == 10:
        FullCode.objects.create(name=data["name"], code=data["code"], import_poduct=data["import"],
                                export_poduct=data["export"], nds_poduct=data["nds"])
    elif not "sub_group" in data.keys():
        create_object(data)
    elif "sub_group" in data.keys():
        create_object(data)
        for i in data["sub_group"]:
            add_db(i)


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


class getDT(APIView):

    def post(self, request):
        print(request.data)
        dt = DT.objects.create(id=request.data.get("id"), source=request.data.get("source"),
                               dist=request.data.get("dist"))
        for i in request.data.get("product"):
            predict_code, detail_predict  = model.predict(i.get("descript"))
            product = Product.objects.create(dt=dt, n_product=i.get("n_declaration"), descript=i.get("descript"),
                                             dt_code=i.get("code"),
                                             price=i.get("price"))
            for code, probability in predict_code:
                PredictClass.objects.create(product=product, predict_code=code, probability=probability)
            for code in detail_predict:
                PredictFullCode.objects.create(product=product, predict_code=code)
        return Response(status=200, data={"status": True})
