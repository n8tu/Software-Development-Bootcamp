from django.shortcuts import render , redirect
from .models import Order, Product


def index(request):

    if 'Cart' not in request.session: #
        request.session['Cart'] = []
    
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def addToCart(request,order):
    is_same = False
    for _order in request.session['Cart']:
        if _order['product_name'] == request.POST['product_name']:
            _order['product_quantity'] += int(request.POST['quantity'])
            is_same = True
            break

    if not is_same:
        request.session['Cart'].append(order)
    request.session.save()



def checkout(request):

    if 'Cart' not in request.session:
        return redirect('/')

    if request.method == 'POST':

        product = Product.objects.get(id=request.POST['product_id'])
        order = {
            "product_name": product.description,
            "product_price": float(product.price),
            "product_quantity": int(request.POST['quantity'])
        }

        addToCart(request,order)
        # For loop to count all quanities in Session # 
        totalQuantity = 0
        totalPaid = 0
        for eachOrder in request.session['Cart']:
            totalQuantity += eachOrder['product_quantity']
            totalPaid += eachOrder['product_quantity'] * (eachOrder['product_price'])
        
        _order = Order.objects.create(
            quantity_ordered = totalQuantity,
            total_price = totalPaid
        )
        _order.save()


        # For loop to count all quanities in Database => Modal Order  # 
        totalQuantity = 0
        totalPaid = 0
        all_orders = Order.objects.all()
        for order in all_orders:
            totalQuantity += order.quantity_ordered
            totalPaid += order.total_price

        del request.session['Cart']

        context = {
        "lastOrderPrice":int(request.POST['quantity']) * float(product.price),
        "totalQuantity":totalQuantity,
        "totalPaid":totalPaid
        }
        return render(request, "store/checkout.html",context)

    else:
        return redirect('/')

