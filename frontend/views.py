from django.shortcuts import render,redirect
from sapp.models import  sdb,prodb
from frontend.models import cdb,redb,cadb

# Create your views here.
def homepage(request):
    cat= sdb.objects.all
    return render(request,"home.html",{'cat':cat})
def pro_page(request):
    pro= prodb.objects.all()
    return render(request,"product.html",{'pro':pro})
def filter_pro(request,filtid):
    filt=prodb.objects.filter(cname=filtid)
    return render(request,"filter.html",{'filt':filt})
def single_pro(request,prod_id):
    data_pro=prodb.objects.get(id=prod_id)
    return render(request,"singleproduct.html",{'data_pro':data_pro})
def about_page(request):
    return render(request,"about.html")
def contact_page(request):
    return render(request,"contact.html")
def savecontact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        su=request.POST.get('subject')
        mess=request.POST.get('message')
        obj=cdb(name=na,email=em,subject=su,message=mess)
        obj.save()
        return redirect(contact_page)
def register_user(request):
    return render(request,"register.html")
def saveregister(request):
    if request.method=="POST":
        na=request.POST.get('name')
        u_s=request.POST.get('username')
        mobile=request.POST.get('mobile')
        emai=request.POST.get('email')
        passw=request.POST.get('password')
        obj=redb(name=na,username=u_s,mobile=mobile,email=emai,password=passw)
        obj.save()
        return redirect(register_user)
def user_login(request):
    if request.method=="POST":
        u_n=request.POST.get('user_name')
        pa_ss=request.POST.get('pass_word')
        if redb.objects.filter(username=u_n,password=pa_ss).exists():
            request.session['username']=u_n
            request.session['password']=pa_ss
            return redirect(homepage)
        else:
            return redirect(register_user)
    else:
        return redirect(register_user)

def log_out(request):
    del request.session['username']
    del request.session['password']
    return redirect(user_login)
def cartpage(request):
    cart=cadb.objects.all()
    return render(request,"cart.html",{'cart':cart})
def cartsave(request):
    if request.method=="POST":
        p=request.POST.get('productname')
        pp=request.POST.get('price')
        pq=request.POST.get('quantity')
        pt=request.POST.get('total price')
        obj=cadb(ctn=p,ctp=pp,ctq=pq,ctt=pt)
        obj.save()
        return redirect(cartpage)



