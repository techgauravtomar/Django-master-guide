"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp.views import*
from django.contrib.auth import login
from django.contrib.auth import logout




from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [     
    path('admin/', admin.site.urls),    
    path('myapp/',include('myapp.urls')),
    path('',home,name='home'),
    path('about-us/',aboutus, name="about"),
    path('contact-us/',contactus, name="contact"),
    path('booking-us/',booking,name="booking"),
    path('service-us/',service,name="service"),
    path('team-us/',team,name="team"),
    
    path('details/',details,name="details"),
    path('details/<int:id>',details,name="details"), 
    path('register-us/',register, name="register"), 
    path('signup-us/',signup, name="signup"),
    path('registration-us/',registration, name="registration"),
    
    # data facting
    path('getall/',getalldata,name="getalldata"),
    # dynamically get data
    path('getdetail/<int:id>',getdetail,name="getdetail"),
    # updatedetail
    path('updatedetail/<int:id>',updatedetail,name="updatedetail"),
    # deletedetail
    path('deletedetail/<int:id>',deletedetail,name="deletedetail"),
    
    # rederiction
    path('thanks/<name>',thanks, name="thanks"),
    path('profile/',profile, name="profile"),
    
    #upload
    path('upload/',upload, name="upload"),
    # download
    path('download/<int:page>',download, name="download"),
    #imagedescription
    path('imagedescription/<int:id>',description, name="description"),
    path('downloaded/<int:document_id>',dowloaded,name='downloaded'),
    path("upload_to_model/<int:page>",upload_to_model,name="upload_to_model"),
    
    path('setcookie/',setcookie),
    path('getcookie/',getcookie),
    path('login/',login ),
    path('logout/',logout),
    
    
    path('connection/',formView, name = 'loginform'),
    path('logout/', logout, name = 'logout'),
    path('login/', login, name = 'login'),
    
    
    path('createview/',StudentCreateView.as_view(),name="createview"),
    path('listview/',StudentListView.as_view(),name="listview"),
    path('retrieve/<int:pk>',StudentDetailView.as_view(),name="detailview"),
    path('weather/', include('myapp.urls')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_frames')),
    path('api/<int:id>',StudentView.as_view()),
    path('api/',StudentView.as_view())
]




