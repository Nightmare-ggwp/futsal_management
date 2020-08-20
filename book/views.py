from django.shortcuts import render,redirect
from book.models import Book
from book.forms import BookForm
from authenticate import Authentication
from authenticate_customer import Authentication
# Create your views here.
@Authentication.valid_customer
def index(request):
    books=Book.objects.all()
    print(books)
    return render(request,'book/index.html',{'books':books})

@Authentication.valid_customer
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=BookForm(request.POST)
        form.save()
        request.session.clear()
        return redirect("/")
