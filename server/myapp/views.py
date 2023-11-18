from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from.forms import studentform
from .models import StudentModel, Movie
from .forms import StudentModelform,MovieForm,LoginForm
import os
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
import datetime
from django.template import RequestContext
from django.template import loader
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,FormView,DetailView
from django.urls import reverse_lazy
import requests
import json
from datetime import datetime


# Create your views here.

def home(request):
    #return HttpResponse(html)
    return render(request,"index.html")

def aboutus(request):
    # return HttpResponse("This is about Us page")
    return render(request,"about.html")

def contactus(request):
    # return HttpResponse("This is contact Us page")
    return render(request,"contact.html")

def service(request):
    # return HttpResponse("This is services page")
    return render(request,"service.html")

def booking(request):
    # return HttpResponse("This is booking page")
    return render(request,"booking.html")

def team(request):
    # return HttpResponse("This is team page")
    return render(request,"team.html")

def details(request,id=None):
#     #return HttpResponse("My id is"+str(id))
    #   d={'id':id,'name':'Gaurav','company':'Ducat'}
        # d={'name':['Rahul','Gaurav','Ajay','Amit']}
      # d={"data":[{'id':1,'name':'Gaurav','company':'Ducat'},{'id':2,'name':'Amit','company':'TCS'},{'id':3,'name':'Ajay','company':'IBM'}]}
       
        d={"card":['Id','Name','Company','DOB','Date','City','State',]}
        return render(request,'details.html',d,)

def register(request):
    stu=StudentModel()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        c_password=request.POST.get("confirm_password")
        stu.name=name
        stu.email=email
        stu.password=password
        stu.confirm_pass=c_password
        stu.save()
        
        print(name,email,password,c_password)
    return render(request,"register.html")


def signup(request):
    stu=StudentModel()
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            stu.name=form.cleaned_data.get('name')
            stu.email=form.cleaned_data.get('email')
            stu.password=form.cleaned_data.get('password')
            stu.confirm_pass=form.cleaned_data.get('confirm_pass')
            stu.save()
            return HttpResponseRedirect('/thanks/{}'.format(stu.name))
        else:
            print("Invalid form submission")
    else:
        form=studentform()
            
    return render(request,"signup.html",{'form':form})

def registration(request):
    form=StudentModelform()
    return render(request,"registration.html",{'form':form})
## all data transfer an another page
def profile(request):
    if request.method=="POST":
        form=StudentModelform(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            data={'name':name,'email':email}
            form.save()  
            return render(request,"profile.html",data)

# data fec
def getalldata(request):
    data=StudentModel.objects.all()
    return render(request,"alldetails.html",{'data':data})
# dynamically get data
def getdetail(requset,id):
    data=StudentModel.objects.get(id=id)
    return render(requset,"getdetail.html",{'data':data})
# Update data
def updatedetail(requset,id):
    data=StudentModel.objects.get(id=id)
    if requset.method=='POST':
        form=StudentModelform(requset.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/getall/")
    else:
       form=StudentModelform(instance=data)
    return render(requset,"updatedetail.html",{'form':form})

# deletedetail
def deletedetail(requset,id):
    try:
       data=StudentModel.objects.get(id=id)
       if requset.method=="POSt":
         data.delete()
         return HttpResponseRedirect("/getall/")
    except:
        return HttpResponse("Details does not exists")
    return render(requset,"deletedetail.html")

# redriection
def thanks(request,name):
    return render(request,"thanks.html",{'data':name})

##upload
def upload(request):
    if request.method=="POST":
        form=MovieForm(request.POST,request.FILES)
        if form.is_valid():
            des=form.cleaned_data.get('description')
            print(des)
            form.save()
        else:
            print("NOt")
    else:
        form=MovieForm()
    return render(request,"upload.html",{'form':form})
        
   
def download(request,page):
    data=Movie.objects.all()
    paginator=Paginator(data,per_page=3)
    page_object=paginator.get_page(page)
    return render(request,template_name="download.html",context={'page_object':page_object,'movies':data})    
    
#imagedescription
def description(request,id):
    data=Movie.objects.get(id=id)
    return render(request,"imagedescription.html",{'data':data})

def dowloaded(request,document_id):
    document=get_object_or_404(Movie,pk=document_id)
    response=HttpResponse(document.image,content_type='application/image')
    response['Content-Disposition']=f'attachment; filename="{document.image.name}"'
    return response

def upload_to_model(request,page):
    movies=Movie.objects.all()
    paginator=Paginator(movies,per_page=3)
    page_object=paginator.get_page(page)
    return render(request,"download.html",context={'page_object':page_object,'movies':movies})    
    
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial','javatpoint.com')
    return response

def getcookie(request):
    try:
       tutorial = request.COOKIES['java-tutorial']
       return HttpResponse("java tutorial @:"+ tutorial)
    except:
        return HttpResponse("No user found")
    
# def LoginForm(request):
#     return render(request, "login.html")
 
# def login(request):
#    username = "not logged in"
   
#    if request.method == "POST":
#       #Get the posted form
#       MyLoginForm = LoginForm(request.POST)
   
#    if MyLoginForm.is_valid():
#       username = MyLoginForm.cleaned_data['username']
#    else:
#       MyLoginForm = LoginForm()
   
#    response = render(request, 'loggedin.html', {"username" : username,"form":LoginForm}, 
#       context_instance = RequestContext(request))
   
#    response.set_cookie('last_connection', datetime.datetime.now())
#    response.set_cookie('username', datetime.datetime.now())
	
#    return response

# def login(request):
#     username = 'not logged in'
#     if request.method == 'POST':
#         MyLoginForm = LoginForm(request.POST)
        
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#     else:
#         MyLoginForm = LoginForm()
#     return render (request,'loggedin.html', {"username" : username})



def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
   
      if MyLoginForm.is_valid():
       username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
   
   response = render(request, 'loggedin.html', {"username" : username}, 
      context_instance = RequestContext(request))
   
   response.set_cookie('last_connection', datetime.datetime.now())
   response.set_cookie('username', datetime.datetime.now())
	
   return response


def formView(request):
    MyLoginForm=LoginForm()
    if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
         "%Y-%m-%d %H:%M:%S")
      
      if (datetime.datetime.now() - last_connection_time).seconds < 10:
         return render(request, 'loggedin.html', {"username" : username})
      else:
         return render(request, 'login.html', {"form" : MyLoginForm})
			
    else:
      return render(request, 'login.html', {"form" : MyLoginForm})

#session

def login(request):
   username = 'not logged in'
   
   if request.method == 'POST':
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
      else:
         MyLoginForm = LoginForm()
			
   return render(request, 'loggedin.html', {"username" : username})

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})
  
  
  

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")




  
  


class StudentCreateView(CreateView):
    model = StudentModel
    fields = '__all__'
    success_url = reverse_lazy('index')
    
class StudentListView(ListView):
    model = StudentModel
    
class StudentDetailView(DetailView):
    model = StudentModel

 
 
 
    

def index(request):
    # the render function is for rendering templates
    return render(request, 'home.html')

   
def index(request):
    # if there are no errors the code inside try will execute
    try:
    # checking if the method is POST
        if request.method == 'POST':
            API_KEY = 'd968d7408f42f24ff306520b0a85cfb3'
            # getting the city name from the form input   
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json   
            response = requests.get(url).json()
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary
            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        # if the request method is GET empty the dictionary
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'home.html', context)
     # if there is an error the 404 page will be rendered 
     # the except will catch all the errors 
    except:
        return render(request, '404.html')
    
    
    

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import StudentSerializer
from rest_framework import permissions   
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class StudentView(APIView):
    """This endpoint list all of the available myapp from the database"""
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,id=None):
        if id:
            result = StudentModel.objects.get(id=id)
            serializer = StudentSerializer(result)
            return Response({'success':'success',"students":serializer.data},status=200)
        else:
         result = StudentModel.objects.all()
         serializer = StudentSerializer(result,many=True)
        
        return Response({'success':'success',"students":serializer.data},status=200)
        
    def Post(self,request):
     serializer = StudentSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response({"status":"success","data":serializer.data})
     else:
         return Response({"status":"error","data":serializer.errors})

    def patch(self,request,id=None):
     result= StudentModel.objects.get(id=id)
     serializer = StudentSerializer(result, data=request.data, partial=True)
     if serializer.is_valid():
         serializer.save()
         return Response({"status":"success","data":serializer.data})
     else:
         return Response({"status":"error","data":serializer.errors})

    def Delete(self,request,id=None):
     result = get_object_or_404(StudentModel, id=id)
     result.delete()
     return Response({"status":"success","data":"Record Deleted"})
     
    
    
    
    
    
    
    
    
    
    
    
    
 