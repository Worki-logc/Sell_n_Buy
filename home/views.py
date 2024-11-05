from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import product, Cart, cart_item
from .forms import productForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new user
            return redirect('/login')  # Replace 'login' with the name of your login route
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def loginUser(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Userpassword = request.POST.get("password")
        user = authenticate(username=Username, password=Userpassword)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect("/login")

@login_required(login_url='/login')
def deleteUser(request):
    user = request.user
    user.delete()
    return redirect("/login")

def product_list(request):
    products = product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required(login_url='/login')
def add_product(request):
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = productForm()
    return render(request, 'add_product.html', {'form': form})

@login_required(login_url='/login')
def dashboard(request):
    products = product.objects.filter(user = request.user)
    return render(request, "dashboard.html", {"products":products})

@login_required(login_url='/login')
def deleteProduct(request, product_id):
    Product = get_object_or_404(product, id=product_id)
    if request.user == Product.user:
        if Product.pic:
            Product.pic.delete(save=False)
        Product.delete()
    return redirect("/dashboard")

@login_required(login_url='/login')
def add_to_cart(request, product_id):
    Product = get_object_or_404(product, id=product_id)
    cart, created = Cart.objects.get_or_create(user = request.user)
    CartItem, created = cart_item.objects.get_or_create(cart=cart, product=Product)

    if not created:
        CartItem.quantity += 1  # Increase quantity if already in the cart
    CartItem.save()

    return redirect("/")

@login_required(login_url='/login')
def cart_details(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})

@login_required(login_url='/login')
def remove_cartItem(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    CartItem = get_object_or_404(cart_item, cart=cart, product_id=product_id)
    CartItem.delete()
    return redirect("/cart")