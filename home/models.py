from django.db import models

# Create your models here.
class Contact(models.Model):
    First_Name= models.CharField(max_length=122)
    Last_Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Phone_Number = models.CharField(max_length=122)
    Street_No = models.CharField(max_length=122)
    Street_Name = models.CharField(max_length=122)
    Street_Type = models.CharField(max_length=122)
    Suburb = models.CharField(max_length=122)
    Postcode = models.CharField(max_length=122)
    State = models.CharField(max_length=122)
    Brand = models.CharField(max_length=122)
    Type = models.CharField(max_length=122)
    Flavor = models.CharField(max_length=122)
    BarcodeNumber = models.CharField(max_length=122)
    BatchCode = models.CharField(max_length=122)
    Retailer_Name = models.CharField(max_length=122)
    Retailer_Location = models.CharField(max_length=122)
    Best_Before_Date = models.CharField(max_length=122)
    Manufacturing_Time = models.CharField(max_length=122)
    Attachment = models.CharField(max_length=122)
    Message = models.CharField(max_length=122)
    submit = models.CharField(max_length=122)

    def __str__(self):
        return self.First_Name