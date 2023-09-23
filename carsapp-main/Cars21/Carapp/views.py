from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Carapp.models import Cars
# Create your views here.
def register(request):
	return render(request,'register.html')

def NewCar(request):
	return render(request,'NewCar.html')

def savedata(request):
	cname=request.GET.get('cname')
	ccompany=request.GET.get('ccompany')
	cmodel=request.GET.get('cmodel')
	cprice=request.GET.get('cprice')
	color=request.GET.get('color')
	p=Cars(cname=cname,ccompany=ccompany,cmodel=cmodel,cprice=cprice,color=color)
	p.save()
	data=Cars.objects.all()
	return render(request,'DisplayCar.html',{'data':data})

def DisplayCar(request):
	data=Cars.objects.all()
	return render(request,'DisplayCar.html',{'data':data})


def FilterCar(request):
	data = Cars.objects.filter(ccompany='honda')

	return render(request,'DisplayCar1.html',{'data':data})
