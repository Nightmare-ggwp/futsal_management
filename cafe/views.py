from django.shortcuts import render,redirect
from cafe.models import Cafe
from cafe.forms import CafeForm
from authenticate import Authentication
# Create your views here.
#@Authentication.valid_user
def index(request):
    print(request.method)
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    cafe=Cafe.objects.raw("select * from cafe limit 4 offset %s",[offset])
    pageItem=len(cafe)
    return render(request,"cafe/index.html",{'cafe':cafe,'page':page,'pageItem':pageItem})

#@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=CafeForm(request.POST,request.FILES)
        form.save()
        return redirect("/cafe")
    else:
        form=CafeForm()
    return render(request,"cafe/create.html",{'form':form})

#@Authentication.valid_user_where_id
def update(request,id):
    cafe=Cafe.objects.get(cafe_id=id)
    if request.method=="POST":
        form=CafeForm(request.POST,request.FILES,instance=cafe)
        form.save()
        return redirect("/cafe")
    else:
        form=CafeForm(instance=cafe)
    return render(request,"cafe/edit.html",{'form':form})

#@Authentication.valid_user_where_id
def delete(request,id):
    cafe=Cafe.objects.get(cafe_id=id)
    cafe.delete()
    return redirect("/cafe")