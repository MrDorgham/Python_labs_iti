from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from bookshop.models import bkinfo
# Create your views here.

def bshop(request):
    return render(request,"bookshop/bshop.html")

def booksinfo(request):
    bookinf = bkinfo.objects.all()
    return render (request, "bookshop/booksinfo.html", context={"bookinf":bookinf})

def contactus(request):
    # return HttpResponse (str("<h1> For Any Information:<h1>") + str("<h1>WhatsApp Number : +20 10 1161 9290<h1>") + str("Email : husseinghoraba.gh@gmail.com"))
    return render(request,"bookshop/contactus.html")

def aboutus(request):
    return render(request,"bookshop/aboutus.html")

def showbook(request, id):
    # bookinf = bkinfo.objects.get(id=id)
    bookinf = get_object_or_404(bkinfo, pk=id)
    return render (request, "bookshop/showbook.html", context={"bookinfo":bookinf})
    
def deletebook(request, id):
    delbook = bkinfo.objects.get(id=id)
    delbook.delete()
    # return HttpResponse("deleted")
    return redirect("booksinfo")
    

     