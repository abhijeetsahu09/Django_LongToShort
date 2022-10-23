from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .models import LongToShort,details
import json
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello,world.")

def home_page(request):

     context = {
         "submitted" : False,
          "error": False
       }
     if request.method in 'POST':

        
        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']

        print(long_url)
        print(custom_name)
        
        # CREATE
        try:
          obj = LongToShort(long_url = long_url, short_url = custom_name)
          obj.save()

          #READ
          date = obj.date
          clicks = obj.clicks

          context["long_url"] = long_url
          context["short_url"] = request.build_absolute_uri() + custom_name
          context["date"] = date
          context["submitted"] = True
          context["clicks"]  = clicks
        except:
          context["error"] = True
        

  
        
     else:
        print("User not sending anything")
       
       
     return render(request,'index.html',context)

def redirect_url(request, short_url):
   row = LongToShort.objects.filter(short_url = short_url)
   if len(row) == 0:
      return HttpResponse("No such short url exist")
   obj = row[0] 
   long_url = obj.long_url  

   obj.clicks = obj.clicks + 1
   obj.save()
   
   return redirect(long_url)


def task(request):

   context = { 
     "my_name" : "John",
     "x" : 15
}

   return render(request, "test.html",context)


def all_analytics(request):
   rows = LongToShort.objects.all()
   
   context = {
      "rows": rows
   }
   return render(request, 'all-analytics.html',context)


def detail(request):
   context = {}
#    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
#    if x_forw_for is not None:
#          ip = x_forw_for.split(',')[0]
#    else:
#          ip = request.META.get('REMOTE_ADDR')
   
#    if 'ip' in request.GET:
#         name = request.GET['ip']
#         url = 'http://ip-api.com/json/%s' % name
#         response = requests.get(url)
#         data = response.json()
#         meals = data['meals']
#         for i in meals:
#          meal_data = details(
#             country = i['country'],
#             state = i['countryCode'],
#             city = i['city']
#          )
#          meal_data.save()
#          print(meal_data)
#          context = details.objects.all().order_by('-id')
#    return render(request,'details.html',{"context": context})


   #getting location
   # id = ip
   # res = requests.get(f'http://ip-api.com/json/{id}')
   # location_data_one = res.text
   # location_data = json.loads(location_data_one)
   # print(location_data)
    
   # return render(request,'details.html')   
   # object = details(location_data)
   # object.save() 
   # country = object.country
   # state = object.timezone
   # city = object.city