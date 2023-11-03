from django.shortcuts import render,redirect
from sapp.models import sdb,prodb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from frontend.models import cdb

# Create your views here.

def indexpage(request):
    return render(request,"index.html")
def addcat(request):
    return render(request,"addcategory.html")
def savedata(request):
    if request.method=="POST":
        cn=request.POST.get('name')
        cd=request.POST.get('description')
        im=request.FILES['image']
        obj=sdb(name=cn,dis=cd,img=im)
        obj.save()
        return redirect(addcat)
def displaydata(request):
    data=sdb.objects.all()
    return render(request,"display.html",{'data':data})
def editdata(request,sid):
    sdata=sdb.objects.get(id=sid)
    return render(request,"edit.html",{'sdata':sdata})
def updatedata(request,sid):
    if request.method=="POST":
        na=request.POST.get('name')
        di=request.POST.get('discription')
        try:
           img=request.FILES['image']
           fs = FileSystemStorage()
           file = fs.save(img.name,img)
        except MultiValueDictKeyError:
           file =sdb.objects.get(id=sid).img
        sdb.objects.filter(id=sid).update(name=na,dis=di,img=file)
        return redirect(displaydata)
def deletedata(request,sid):
    sdata=sdb.objects.filter(id=sid)
    sdata.delete()
    return redirect(displaydata)
def productdata(request):
    category=sdb.objects.all()
    return render(request,"addproduct.html",{'category':category})
def savepro(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        snam = request.POST.get('Name')
        sdisc = request.POST.get('description')
        spri = request.POST.get('price')
        simg = request.FILES['profile']
        obj = prodb(cname=nam, sname=snam, sdis=sdisc, spr=spri, sim=simg)
        obj.save()
        return redirect(productdata)
def displaypro(request):
    sdata=prodb.objects.all()
    return render(request,"displaypro.html",{'sdata':sdata})
def editpro(request,eid):
    sdata=sdb.objects.all()
    pro = prodb.objects.get(id=eid)
    return render(request, "editpro.html", {'sdata':sdata,'pro':pro})
def updatecat(request,eid):
    if request.method=="POST":
        ca=request.POST.get('category')
        pn=request.POST.get('Name')
        pd=request.POST.get('description')
        pp=request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = prodb.objects.get(id=eid).sim
        prodb.objects.filter(id=eid).update(cname=ca,sname=pn,sdis=pd,spr=pp,sim=file)
        return redirect(displaypro)

def deletepro(request,eid):
    service= prodb.objects.filter(id=eid)
    service.delete()
    return redirect(displaypro)
def loginpage(request):
    return render(request,"adminlogin.html")
def admin_login(request):
    if request.method=="POST":
        una=request.POST.get('user_name')
        pa=request.POST.get('pass_word')
        if User.objects.filter(username__contains=una).exists():
            x=authenticate(username=una,password=pa)
            if x is not None:
                login(request,x)
                request.session['username']=una
                request.session['password']=pa
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def contact_dispaly(request):
    con=cdb.objects.all()
    return render(request,"contact_user.html",{'con':con})
def delete_user(request,uid):
    use_r=cdb.objects.filter(id=uid)
    use_r.delete()
    return redirect(contact_dispaly)



