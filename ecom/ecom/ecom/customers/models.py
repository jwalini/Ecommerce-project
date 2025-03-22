from django.db import models

class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    landmark = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country} - {self.pincode}"

class User(models.Model):  
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
