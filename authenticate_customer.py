from django.shortcuts import redirect
from user.models import User
from customer.models import Customer
from django.contrib import messages
#class where authentication is done
class Authentication:
    def valid_customer(function):
        def wrap(request):
            print(request)
            try:
                Customer.objects.get(username=request.session['username'], password = request.session['password'])

                return function(request)
            except:

                messages.warning(request,'Please enter valid username and password')
            return redirect('/register')
        return wrap

    def valid_customer_where_id(function):
        def wrap(request,id):
             try:
                Customer.objects.get(username=request.session['username'], password = request.session['password'])
                return function(request,id)
             except:
                messages.warning(request,'Please enter valid username and password')
                return redirect('/register')
        return wrap

