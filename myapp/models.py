from django.db import models

# Create your models here.

class ClientRequest(models.Model):
    name = models.CharField(max_length=150, help_text="name of the client")
    email = models.CharField(max_length=150, help_text="email of the client")
    phone =  models.CharField(max_length=150, help_text="phone number of the client")
    requirement = models.CharField(max_length=150, help_text="requirement of the client")

    class Meta:
        db_table = "client_request"



