from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Dress
from .forms import DressForm
# Create your views here.

def index(request):
    dress=Dress.objects.all()
    context={
        'dress_list':dress
    }
    return render(request,'index.html',context)
# Create your views here.
def detail(request,dress_id):
    dress= Dress.objects.get(id= dress_id)
    return render(request,"detail.html",{'dress': dress})


def add_dress(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        brand = request.POST.get('brand', )
        price = request.POST.get('price', )
        img = request.FILES['img']
        dress = Dress(name=name,desc=desc,brand=brand,price=price,img=img)
        dress.save();
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    dress=Dress.objects.get(id=id)
    form=DressForm(request.POST or None ,request.FILES,instance=dress)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'dress':dress })


def delete(request,id):
    if request.method=='POST':
        dress = Dress.objects.get(id=id)
        dress.delete()
        return redirect('/')
    return render(request,'delete.html')


# Create your views here.

