from django.shortcuts import render

# Create your views here.
def forloop (request):
    d={'name':'BANGARAM','hey':'STALKER'}
    return render(request,'forloop.html',d)
