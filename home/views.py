from django.shortcuts import render,redirect
from ground.models import Ground
from customer.forms import CustomerForm
# Create your views here.
def index(request):
    grounds=Ground.objects.all()
    return render(request,'home/index.html' ,{'grounds':grounds})

def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        result=form.save()
        request.session['customer_id']=result.customer_id
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"home/register.html",{'form':form})

def login(request):

    if(request.method=='POST'):
       request.session['email']=request.POST['email']
       request.session['password']=request.POST['password']

       return redirect("/user")

    return render(request,"home/login.html")

def login_customer(request):

    if(request.method=='POST'):
       request.session['username']=request.POST['username']
       request.session['password']=request.POST['password']
       print('CUSTOMER')

       return redirect("/")
    return render(request,"home/login_customer.html")


def logout(request):
    request.session.clear()
    return redirect("/")

def view_details(request):
    grounds = Ground.objects.all()
    return render(request, "home/test.html", {'grounds':grounds})