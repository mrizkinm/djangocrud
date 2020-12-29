from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName = models.CharField("First name", max_length=255, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.firstName

class Cars(models.Model):
    carsName = models.CharField("Cars name", max_length=255, blank = False, null = False)
    brand = models.CharField("Brand name", max_length=255, blank = False, null = False, default="")
    price = models.IntegerField(default=0)
    color = models.CharField("Color", max_length=255, blank = False, null = False, default="")
    Carype = models.CharField("Types", max_length=255, blank = False, null = False, default="") 
    plat = models.CharField("Plat", max_length= 10, blank = False, default="")
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    status = models.BooleanField()

    def __str__(self):
        return self.carsName

class Rent(models.Model):
    idCars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    # idContact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False, null = False)
    rentDate = models.DateTimeField("Rent Date", auto_now_add=True)
    rentDateBack = models.DateTimeField("Rent Date Back", auto_now_add=True)
    plat = models.CharField("Plat", max_length= 10, blank = False, default="")
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    updatedAt = models.DateTimeField("Updated At", auto_now_add=True)

    def __str__(self):
        return self.carsName