from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    client_name = models.CharField(max_length=50, null=True, default=None)
    client_passport = models.CharField(max_length=11, null=True, default=None)
    client_birthday = models.DateField(null=True, default=None)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_cost = models.FloatField()
    product_made = models.CharField(max_length=20)
    product_category = models.CharField(max_length=50)


class Branch(models.Model):
    branch_address = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='BranchProduct')


class Manager(models.Model):
    manager_name = models.CharField(max_length=50)
    manager_birthday = models.DateField()
    manager_recruitment = models.DateField()
    manager_salary = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,)
    user = models.OneToOneField(User, default=None)


class Auto(models.Model):
    auto_model = models.CharField(max_length=50)
    auto_number = models.CharField(max_length=15)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,)


class Driver(models.Model):
    driver_name = models.CharField(max_length=50)
    driver_birthday = models.DateField()
    driver_salary = models.IntegerField()
    driver_recruitment = models.DateField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE,)


class OrderTable(models.Model):
    order_date = models.DateField()
    order_address = models.CharField(null=True, default=None, max_length=50)
    order_totalcost = models.FloatField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE,)
    client = models.ForeignKey(
        Client, null=True, default=None, on_delete=models.CASCADE,)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,)
    auto = models.ForeignKey(
        Auto, null=True, default=None, on_delete=models.CASCADE,)
    products = models.ManyToManyField(Product, through='OrderProduct')


class BranchProduct(models.Model):
    product_rest = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)


class OrderProduct(models.Model):
    product_count = models.IntegerField()
    ordertable = models.ForeignKey(OrderTable, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
