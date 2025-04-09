from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender=models.CharField(max_length=10)
    phone_number=models.IntegerField(max_length=10)

    def str(self):
        return self.name
