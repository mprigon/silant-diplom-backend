from django.db import models
from django.contrib.auth.models import User


class Loader(models.Model):
    serialNumber = models.CharField(max_length=64)
    modelOfLoader = models.ForeignKey('ModelLoader', on_delete=models.PROTECT)
    modelOfEngine = models.ForeignKey('ModelEngine', on_delete=models.PROTECT)
    serialNumberEngine = models.CharField(max_length=64)
    modelOfTransmission = models.ForeignKey('ModelTransmission', on_delete=models.PROTECT)
    serialNumberTransmission = models.CharField(max_length=64)
    modelOfLeadingAxle = models.ForeignKey('ModelLeadingAxle', on_delete=models.PROTECT)
    serialNumberLeadingAxle = models.CharField(max_length=64)
    modelOfSteerAxle = models.ForeignKey('ModelSteerAxle', on_delete=models.PROTECT)
    serialNumberSteerAxle = models.CharField(max_length=64)
    supplyContractNumDate = models.CharField(max_length=64)
    dateOfShippingFactory = models.DateField()
    recipient = models.CharField(max_length=64)
    deliveryAddress = models.CharField(max_length=128)
    equipment = models.CharField(max_length=64)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    serviceCompanyLoader = models.ForeignKey('ServiceCompany', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serialNumber}'


class ModelLoader(models.Model):
    nameModelLoader = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameModelLoader}'


class ModelEngine(models.Model):
    nameModelEngine = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameModelEngine}'


class ModelTransmission(models.Model):
    nameModelTransmission = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameModelTransmission}'


class ModelLeadingAxle(models.Model):
    nameModelLeadingAxle = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameModelLeadingAxle}'


class ModelSteerAxle(models.Model):
    nameModelSteerAxle = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameModelSteerAxle}'


class Client(models.Model):
    loaderClient = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.loaderClient}'


class ServiceCompany(models.Model):
    authServiceCompany = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.authServiceCompany}'


class TechService(models.Model):
    typeTechService = models.CharField(max_length=128)
    dateTechService = models.DateField()
    operatingTimeTech = models.FloatField()
    numberWorkOrder = models.CharField(max_length=64)
    dateWorkOrder = models.DateField()
    loaderOnTechService = models.ForeignKey('Loader', on_delete=models.CASCADE)
    # правильно ли on_delete=models.CASCADE
    techServiceCompany = models.ForeignKey('ServiceCompany', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'Вид ТО: {self.typeTechService} дата ТО: {self.dateTechService} Сервисная компания: {self.techServiceCompany} {self.loaderOnTechService}'


class Claims(models.Model):
    dateFailure = models.DateField()
    operatingTimeClaim = models.FloatField()
    unitFailure = models.CharField(max_length=128)
    detailsFailure = models.CharField(max_length=264)
    methodRepair = models.CharField(max_length=128)
    spareParts = models.CharField(max_length=128)
    dateRepair = models.DateField()
    # downTime = dateRepair - dateFailure  # warning что это не работает, нет __sub__
    # pylint не понимает логики Django? Class 'DateField' does not define 'sub'
    # makemigrations не проходит, добавляем @property
    loaderOnClaim = models.ForeignKey('Loader', on_delete=models.CASCADE)
    repairServiceCompany = models.ForeignKey('ServiceCompany', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    @property
    def durationDownTime(self):
        return self.dateRepair - self.dateFailure

    def __str__(self):
        return f'{self.detailsFailure[:64]} Дата неисправности: {self.dateFailure} {self.loaderOnClaim}'

