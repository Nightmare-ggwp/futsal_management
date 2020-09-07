from django.shortcuts import render,redirect
from ground.models import Ground
from customer.models import Customer
from customer.forms import CustomerForm
from ground.forms import GroundForm
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

def logout(request):
    request.session.clear()
    return redirect("/")

def view_details(request,id):
    ground = Ground.objects.get(ground_id=id)
    if request.method == "POST":
        form = GroundForm(request.POST, request.FILES, instance=ground)
        form.save()
        return redirect("/view_details")
    else:
        form = GroundForm(instance=ground)
    return render(request, "home/view_details.html", {'ground': ground, 'form': form})

