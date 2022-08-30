from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product
# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class InsertView(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res=HttpResponse("product inserted succesfully")
        return res

class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,'display.html',con_dic)

class DeleteInputView(View):
    def get(self,request):
        return render(request,'deleteinput.html')
class DeleteView(View):
    def get(self,request):
        P_id=int(request.GET["t1"])
        prod=Product.objects.filter(pid=P_id)
        prod.delete()
        res=HttpResponse("product deleted succesfully")
        return res

class UpdateInputView(View):
    def get(self,request):
        return render(request,"updateinput.html")
class UpdatView(View):
    def post(self,request):
        P_id=int(request.POST["t1"])
        P_name=request.POST["t2"]
        P_cost=float(request.POST["t3"])
        P_mfdt=request.POST["t4"]
        P_expdt=request.POST["t5"]
        prod=Product.objects.get(pid=P_id)
        prod.pname=P_name
        prod.cost=P_cost
        prod.mfdt=P_mfdt
        prod.pexpdt=P_expdt
        prod.save()
        res=HttpResponse('product updated succesfully')
        return res