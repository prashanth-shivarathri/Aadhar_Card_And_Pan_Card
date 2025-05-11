from django.shortcuts import render
from .forms import AadharForm
from .models import Aadhar

# Create your views here.
def home(request):
     form=AadharForm()
     if request.method=='POST':
          form=AadharForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               print("Data added saved successfully.")
               try:
                    data=Aadhar.objects.all().order_by('-aadhar_number')[0]
               except:
                    print("Aadhar number not found")
               return render(request,'display.html',{'data':data})

     return render(request,'index.html',{'form':form})

# def display(request):
#      try:
#           data=Aadhar.objects.all().order_by('-aadhar_number')[0]
#      except:
#           print("Aadhar number not found.")
#      return render(request,'display.html',{'data':data})

#! Live share 
def download(request):
     if request.method=='POST':
          aadhar=request.POST.get('aadhar')
          data=Aadhar.objects.get(aadhar_number=aadhar)
          return render(request,'display.html',{'data':data})

     return render(request,'download.html')

def home_page(request):
     return render(request,'home.html')

def pan(request):
     data=None
     if request.method=='POST':
          aadhar=request.POST.get('aadhar')
          data=Aadhar.objects.get(aadhar_number=aadhar)

          return render(request,'display_pan.html',{'data':data})

     return render(request,'pan.html')

# def diaplay_pan(request):
     
#      return render(request,'display_pan.html',)