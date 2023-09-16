from django.shortcuts import render,HttpResponse
from home.models import Contact
from time import time
from django.contrib.messages import constants as messages

# Create your views here.
def index(request):
    context ={
        "variable":"This is sent"
    }
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        First_Name = request.POST.get('FirstName')
        Last_Name = request.POST.get('LastName')
        Email = request.POST.get('Email')
        Phone_Number = request.POST.get('PhoneNumber')
        Street_No = request.POST.get('StreetNo')
        Street_Name = request.POST.get('StreetName')
        Street_Type = request.POST.get('StreetType')
        Suburb = request.POST.get('Suburb')
        Postcode = request.POST.get('Postcode')
        State = request.POST.get('State')
        Brand = request.POST.get('Brand')
        Type = request.POST.get('Type')
        Flavor = request.POST.get('Flavor')
        BarcodeNumber = request.POST.get('BarcodeNumber')
        BatchCode = request.POST.get('BatchCode')
        Retailer_Name = request.POST.get('RetailerName')
        Retailer_Location = request.POST.get('RetailerLocation')
        Best_Before_Date = request.POST.get('BestBeforeDate')
        Manufacturing_Time = request.POST.get('ManufacturingTime')
        Attachment = request.POST.get('Attachment')
        Message = request.POST.get('Message')
        submit = request.POST.get('submit')
        contact=Contact(First_Name = 'First_Name',Last_Name = 'Last_Name',Email = 'Email' ,Phone_Number = 'Phone_Number' ,Street_No = 'Street_No',Street_Name = 'Street_Name',Street_Type = 'Street_Type',Suburb = 'Suburb',Postcode = 'Postcode' ,State = 'State',Brand = 'Brand',Type = 'Type',Flavor = 'Flavor',
    BarcodeNumber = 'BarcodeNumber',BatchCode = 'BatchCode' ,Retailer_Name = 'Retailer_Name',Retailer_Location = 'Retailer_Location',Best_Before_Date = 'Best_Before_Date',Manufacturing_Time = 'Manufacturing_Time',Attachment = 'Attachment',Message = 'Message',submit = 'submit')
        contact.save()
    return render(request,'contact.html')