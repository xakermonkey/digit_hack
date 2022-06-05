from django import template
from employee.models import *
register = template.Library()



@register.filter(name='get_status')
def get_status(value):
    dt = DT.objects.get(id=value)
    for product in Product.objects.filter(df=dt):
        full_code = PredictFullCode.objects.filter(product=product)
        if full_code:
            if full_code.first().predict_code != product.dt_code:
                return "Различие"
            else:
                return "Совпадение"
        else:
            return "Недостаточно данных"



@register.filter(name='predict_code')
def predict_code(value):
    full_code = PredictFullCode.objects.filter(product=value).first()
    if full_code:
        return full_code.predict_code
    predict = PredictClass.objects.filter(product=value).first()
    return predict.predict_code




@register.filter(name='validation')
def validation(value):
    print(value)
    full_code = PredictFullCode.objects.filter(product=value).first()
    if full_code:
        return full_code.predict_code == value.dt_code
    return False



@register.filter(name='get_import')
def get_import(value):
    return FullCode.objects.filter(code=value).first().import_poduct + "%" if FullCode.objects.filter(code=value).first() else ""



@register.filter(name='get_export')
def get_export(value):
    return FullCode.objects.filter(code=value).first().export_poduct if FullCode.objects.filter(code=value).first() else ""



@register.filter(name='get_nds')
def get_nds(value):
    return FullCode.objects.filter(code=value).first().nds_poduct if FullCode.objects.filter(code=value).first() else ""





