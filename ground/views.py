from django.shortcuts import render,redirect
from ground.models import Ground
from ground.forms import GroundForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
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

    grounds=Ground.objects.raw("select * from ground limit 4 offset %s",[offset])
    pageItem=len(grounds)
    return render(request,"ground/index.html",{'grounds':grounds,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=GroundForm(request.POST,request.FILES)
        form.save()
        return redirect("/ground")
    else:
        form=GroundForm()
    return render(request,"ground/create.html",{'form':form})

@Authentication.valid_user_where_id
def update(request,id):
    ground=Ground.objects.get(ground_id=id)
    if request.method=="POST":
        form=GroundForm(request.POST,request.FILES,instance=ground)
        form.save()
        return redirect("/ground")
    else:
        form=GroundForm(instance=ground)
    return render(request,"ground/edit.html",{'form':form})

@Authentication.valid_user_where_id
def delete(request,id):
    ground=Ground.objects.get(ground_id=id)
    ground.delete()
    return redirect("/ground")