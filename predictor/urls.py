from django.urls import path 
from . import views 
urlpatterns = [ 
	path('breast', views.breast, name="breast"), 
	path('', views.home, name="base"), 
    path('login/', views.userlogin, name="login"), 
    # # path('about/', views.about, name="about"), 
    # path('prediction/', views.prediction, name="prediction"), 
    # path('contact/', views.contact, name="contact"), 
] 
