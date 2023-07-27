from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm

from .models import *
from .form  import *



# Create your views here.

####### User views
@login_required(login_url='user_login')
def dashboard(request):
    sitename = "Homepage"
    homeStyle = "home"

    messagesClass = ''
    created_message_status = request.GET.get('created')
    if created_message_status:
        print(created_message_status)
        messagesClass = 'success'

    updated_message_status = request.GET.get('updated')
    if updated_message_status:
        print(updated_message_status)
        messagesClass = 'success'

    deleted_message_status = request.GET.get('deleted')        
    if deleted_message_status:
        print(deleted_message_status)
        messagesClass = 'danger'

    orders = Order.objects.all()
    users = User.objects.all()
    total_orders = orders.count()
    total_users = users.count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()
    delivered = orders.filter(status='Delivered').count()
    context = {'sitename':sitename, 'style':homeStyle, 'users':users, 'orders':orders, 'total_orders':total_orders, 'total_users':total_users, 'pending':pending, 'out_for_delivery':out_for_delivery, 'delivered':delivered, 'messagesClass':messagesClass} 
    return render(request, 'dashboard.html', context)


def contact(request):
    sitename = "Contact"
    context = {'sitename' : sitename}    
    return render(request, 'contact.html', context)


def about(request):
    sitename = "About-Us"
    context = {'sitename' : sitename}    
    return render(request, 'about.html', context)


####### User views
@login_required(login_url='user_login')
def user_dashboard(request, pk, *args, **kwargs):
    sitename = "User | Dashboard"
    user = User.objects.get(id=pk)
    orders = user.order_set.all()
    context = {'sitename' : sitename, 'user':user, 'orders':orders}    
    return render(request, 'users/user_dashboard.html', context)


def user_register(request):
    sitename = "User | Register"
    if request.user.is_authenticated:
        messages.success(request, 'You are logged in. Please Logout first...')
        return redirect('/?redirect=True')
    else:
        # messagesClass = ''
        # created_message_status = request.GET.get('created')
        # if created_message_status:
        #     print(created_message_status)
        #     messagesClass = 'success'
        # else:
        #     print(created_message_status)
        #     messagesClass = 'danger'
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User created successfully...')
                return redirect('/users/login?created=User Created')
            else:
                messages.warning(request, 'User not created...')
        context = {'sitename' : sitename, 'form':form}    
        return render(request, 'users/user_register.html', context)


def user_login(request):
    sitename = "User | Login"
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in...')
        return redirect('/?redirect=True')
    else:
        if request.method == 'POST':
            username = request.POST['username']     # You can also use request.POST.get('username')
            password = request.POST['password']     # You can also use request.POST.get('password')
            print('DETAILS: ', username, password)
            
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Welcome ' + username)
                return redirect('/')
            else:
                messages.warning(request, 'Incorrect Username OR Password.')
        context = {'sitename' : sitename}    
        return render(request, 'users/user_login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'User logged out successfully...')
    return redirect('user_login')


@login_required(login_url='user_login')
def all_user(request):
    sitename = "All Users"
    users = User.objects.all()
    context = {'sitename':sitename, 'users':users}    
    return render(request, 'users/all_users.html', context)
    

####### Product views
def products(request):
    sitename = "Products"
    products = Product.objects.all()
    context = {'sitename' : sitename, 'products' : products} 
    return render(request, 'product/products.html', context)


def product_details(request):
    sitename = "Products | Details"
    context = {'sitename' : sitename}    
    return render(request, 'product/product_details.html', context)


####### Order views
def checkout(request):
    sitename = "Checkout"
    context = {'sitename' : sitename}    
    return render(request, 'product/checkout.html', context)


@login_required(login_url='user_login')
def create_order(request):
    sitename = "Create Order"
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order has been added successfully')
            return redirect('/?created=True')
    context = {'sitename' : sitename, 'form':form}    
    return render(request, 'product/create_order.html', context)
    # sitename = "Create Order"
    # if request.method == 'POST':
    #     order = Order()
    #     order.user = request.POST.get('user')
    #     order.product = request.POST.get('product')
    #     order.status = request.POST.get('status')
    #     if order.is_valid():
    #         order.save()
    #         return redirect ('/?added=True')



def all_orders(request):
    sitename = "All Orders"
    context = {'sitename' : sitename}    
    return render(request, 'product/all_orders.html', context)


@login_required(login_url='user_login')
def update_order(request, pk):
    sitename = "Update Order"
    update = True
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order has been updated successfully')
            return redirect('/?updated=True')
    context = {'sitename' : sitename, 'form':form, 'update':update}    
    return render(request, 'product/create_order.html', context)


@login_required(login_url='user_login')
def delete_order(request, pk):
    # sitename = "Homepage"
    # homeStyle = "home"
    order = Order.objects.get(id=pk)
    if order is not None:
        order.delete()
        messages.success(request, 'Order deleted successfully...')
        return redirect('/?deleted=True')
    context = {}
    return render(request, 'dashboard.html', context)







# praise god will help on this...
# class NameView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('GET request!')

#     def post(self, request, *args, **kwargs):
#         return HttpResponse('POST request!')

