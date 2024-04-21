from django.shortcuts import render

# Imported to use Http Response
# Hamid
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

# Here we define a function which will return the home page when calling it
# It is called from main URL which is in url.py file
# Hamid
def Home(request):
    return render(request,"app/home.html")


class CategoryView(View):
    def get(self,request,val):
        return render(request,"app/category.html",locals())


