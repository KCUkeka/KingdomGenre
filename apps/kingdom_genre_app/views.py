from django.shortcuts import render, HttpResponse, redirect

def main (request):
    return render (request, 'home.html')

def about (request):
    return render (request, 'about.html')

def sealed_hoodies (request):
    return render (request, 'sealed_hoodies.html')

def sealed_tshirts (request):
    return render (request, 'sealed_tshirts.html')

def kingdom_hoodies (request):
    return render (request, 'kingdom_hoodies.html')

def kingdom_tshirts (request):
    return render (request, 'kingdom_tshirts.html')

def christ_hoodies (request):
    return render (request, 'christ_hoodies.html')

def christ_tshirts (request):
    return render (request, 'christ_tshirts.html')

def contact_us (request):
    return render (request, 'contact_us.html')

