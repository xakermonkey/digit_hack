from django.db import models


# Create your models here.



class Group(models.Model):
    code = models.CharField(max_length=2, verbose_name="Код группы", unique=True, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название группы")
    chapter = models.CharField(max_length=255, verbose_name="Раздел", default="0")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class ProductPosition(models.Model):
    code = models.CharField(max_length=4, verbose_name="Код товарной позиции", unique=True, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название товарной позиции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товарная позиция"
        verbose_name_plural = "товарные позиции"


class SubPosition(models.Model):
    code = models.CharField(max_length=6, verbose_name="Код субпозиции", unique=True, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название субпозиции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Субпозиция"
        verbose_name_plural = "Субпозиции"


class UnderSubPosition(models.Model):
    code = models.CharField(max_length=8, verbose_name="Код подсубпозиции", unique=True, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название подсубпозиции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подсубпозиция"
        verbose_name_plural = "Подсубпозиции"


class FullCode(models.Model):
    code = models.CharField(max_length=10, verbose_name="Полный код товара", unique=True, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название полного кода товара")
    import_poduct = models.CharField(max_length=100,verbose_name="Пошлина на импорт", null=True, blank=True)
    export_poduct = models.CharField(max_length=100,verbose_name="Пошлина на экспорт", null=True, blank=True)
    nds_poduct = models.CharField(max_length=100,verbose_name="НДС", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Полный код товара"
        verbose_name_plural = "Полные коды товаров"



class DT(models.Model):
    source = models.CharField(max_length=255, verbose_name="Отправитель")
    dist = models.CharField(max_length=255, verbose_name="Получатель")

    def __str__(self):
        return f"Декларация на товары № {self.id}"

    class Meta:
        verbose_name="Декларация на товары"
        verbose_name_plural="Декларации на товары"


class Product(models.Model):
    df = models.ForeignKey(DT, on_delete=models.CASCADE, verbose_name="Декларация на товары")
    n_product = models.IntegerField(verbose_name="Номер товара в декларации")
    descript = models.TextField(verbose_name="Описание товара")
    dt_code = models.CharField(max_length=15, verbose_name="Код в декларции")
    # predict_code = models.CharField(max_length=15, verbose_name="Определенный код", null=True, blank=True)
    price = models.CharField(max_length=10, verbose_name="Стоимость товара")

    def __str__(self):
        return f"{self.n_product} товар из декларации на товары № {self.id}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class PredictClass(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    predict_code = models.CharField(max_length=10, verbose_name="Предсказанный код")
    probability = models.IntegerField(verbose_name="Вероятность")


class PredictFullCode(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    predict_code = models.CharField(max_length=10, verbose_name="Предсказанный код")