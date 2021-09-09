from django.db import models

# Create your models here.

class Transactions(models.Model):
    customer_amount = models.IntegerField()
    Business_short_code_db = models.CharField(max_length=100)
    customer_phone_number_db = models.IntegerField()
    company_phone_number_db = models.IntegerField()


    def __str__(self):
        return self.Business_short_code_db