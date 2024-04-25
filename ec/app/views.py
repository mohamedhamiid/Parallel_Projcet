from audioop import reverse
from django.db.models import Count, Q
from django.shortcuts import redirect, render 
from django.views import View
# import razorpay
from .models import Cart, Product,Customer,Payment,OrderPlaced
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#Anas
#sara
from .forms import CustomerProfileForm, CustomerRegistrationForm
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html",locals())
    
class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())
    
# Anas
# add customer registeration view   

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/customerregistration.html',locals())

# Kiro 
# add one class profile view 

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer.objects.create(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            messages.success(request, "Profile saved successfully")
            return render(request, 'app/profile.html', {'form': form, 'success': True})
        else:
            messages.warning(request, "Invalid input data")
        return render(request, 'app/profile.html', {'form': form})

class AddressView(View):
    def get(self, request):
        add = Customer.objects.filter(user=request.user)
        return render(request, 'app/address.html', {'add': add})
    
class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.user = request.user
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.warning(request, "Invalid input data")
        return redirect("address")

        
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    try:
        Cart.objects.get(Q(product=product_id) & Q(user=request.user))
    except:
        Cart(user=user, product=product).save()
    return redirect("/cart")
    
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 20
    return render(request, 'app/addtocart.html', locals())
class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value=p.quantity*p.product.discounted_price
            famount=famount+value
        totalamount= famount+40
        # razoramount=int(totalamount*100)#mult in 100 for rupess????????
        # client=razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        # data={"amount":razoramount,"currency":"INR","receipt":"order_rcptid_11"}
        # payment_response=client.order.create(data=data)
        # print(payment_response)
        # # print output as a comment
        # order_id=payment_response['id']
        # order_status=payment_response['status']
        # if order_status =='created':
        #     payment=Payment(
        #         user=user,
        #         amount=totalamount,
        #         razorpay_order_id=order_id,
        #         razorpay_payment_status=order_status
        #     )
        #     payment.save()
        return render(request, 'app/checkout.html',locals())
    
def test(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    error_message = None
    
    # Handle if quantity isn't valid
    for cart_item in cart_items:
        product = cart_item.product  # Access the product associated with the cart item
        if product.Quantity >= cart_item.quantity:
            product.Quantity -= cart_item.quantity
            product.save()
        else:
            # Quantity is insufficient, set error_message
            error_message = f"The available quantity for {product.title} is only {product.Quantity}. Please remove it from your cart or reduce the quantity."
            break
    
    if error_message:
        return JsonResponse({'message': error_message}, status=400)
    # else:
    #     success_url = reverse('app/home.html')
    #     return JsonResponse({'redirect_url': 'app/home.html'})

def payment_done(request):
    # order_id=request.GET.get('order_id')
    # payment_id=request.GET.get('payment_id')
    # cust_id=request.GET.get('cust_id')
    # user=request.user
    # customer=Customer.objects.get(id=cust_id)
    # payment=Payment.objects.get(razorpay_order=order_id)
    # payment.paid=True
    # payment.razorpay_payment_id=payment_id
    # payment.save()
    # cart=Cart.objects.filter(user=user)
    # for c in cart:
    #     OrderPlaced(user=user,customer=customer, product=c.product,quantity=c.quantity,payment=payment).save()
    #     c.delete()
    return render(request, 'app/paymenttemplatetest.html',locals())    
    
    
    
    
def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 20
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity = max(c.quantity - 1, 0)
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 20
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
    
        return JsonResponse(data)
        
def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 20
        data = {
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)