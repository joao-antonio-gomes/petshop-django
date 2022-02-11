from django.db import models


class Petshop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    website = models.URLField()
    description = models.TextField()


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.JSONField()
    petshop = models.ForeignKey(Petshop, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Employee(User):
    class Meta:
        pass


class Customer(User):
    class Meta:
        pass


class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    petshop = models.ForeignKey(Petshop, on_delete=models.CASCADE)

    class Meta:
        pass


class Procedure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    petshop = models.ForeignKey(Petshop, on_delete=models.CASCADE)

    class Meta:
        pass
