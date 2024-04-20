from django.shortcuts import render

# Imported to use Http Response
# Hamid
from django.http import HttpResponse

# Create your views here.

# Here we define a function which will return the home page when calling it
# It is called from main URL which is in url.py file
# Hamid
def Home(request):
    return render(request,"app/home.html")