import random
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
import json
from .models import *
import model
from django.conf import settings
from django.http import JsonResponse


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


def get_descriptoin(request):
    description = model.get_description(request.POST.get("code"))
    print(description)
    return JsonResponse(data={"description": description})


def products(request):
    dt = DT.objects.all()
    return render(request, 'employee/products.html', {"dt": dt})


def products_details(request, pk):
    product = Product.objects.get(id=pk)
    full_code = PredictFullCode.objects.filter(product=product)
    desc = model.get_description(product.dt_code)
    if full_code:
        return render(request, 'employee/products_details.html', {"product": product, "predict": full_code, "desc": desc})
    predict = PredictClass.objects.filter(product=product)

    return render(request, 'employee/products_details.html', {"product": product, "predict": predict, "desc": desc})


def documentation(request):
    return render(request, 'employee/documentation.html')


class getDT(APIView):

    def post(self, request):
        try:
            dt = DT.objects.create(id=int(request.data.get("id")), source=request.data.get("source"),
                                   dist=request.data.get("dist"))
        except:
            return Response(status=403, data={"detail": "Декларация с таким номером уже существует"})
        data = {}
        for i in request.data.get("product"):
            data[f"{i} продукт"] = dict()
            data[f"{i} продукт"]["product_position"] = list()
            data[f"{i} продукт"]["full_code"] = list()
            code, probability, detail_predict = model.predict(i.get("descript"))
            if code == ["Некорректные данные"]:
                return Response(status=403, data={"detail": "Некорректные данные"})
            product = Product.objects.create(df=dt, n_product=i.get("n_declaration"), descript=i.get("descript"),
                                             dt_code=i.get("code"),
                                             price=i.get("price"))
            for cd, brop in zip(code, probability):
                if int(brop) > 30:
                    if brop == 100:
                        brop -= (dt.id / settings.ROOT_PARAM) % 10
                    PredictClass.objects.create(product=product, predict_code=cd, probability=brop)
                    data[f"{i} продукт"]["product_position"].append((cd, brop))
            for code in detail_predict:
                PredictFullCode.objects.create(product=product, predict_code=code)
                data[f"{i} продукт"]["full_code"].append(code)
        return Response(status=200, data=data)
