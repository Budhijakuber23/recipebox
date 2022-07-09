from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homee.html')

def cake(request):
    return render(request, 'cake.html')

def pizza(request):
    return render(request, 'pizza.html')

def pasta(request):
    return render(request, 'pasta.html')

def contact(request):
    return render(request ,'contact.html')

def noodles(request):
    return render(request ,'noodles.html')

def lasagna(request):
    return render(request ,'lasagna.html')

def sandwich(request):
    return render(request, 'sandwich.html')

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')