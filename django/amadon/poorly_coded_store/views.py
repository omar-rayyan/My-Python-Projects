from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum 

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    item_ordered = Product.objects.get(id=request.POST["product_id"])
    price_from_db = item_ordered.price
    total_charge = quantity_from_form * price_from_db
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    total_quantity_ordered_ever = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum'] or 0
    total_amount_ordered_ever = float(Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0.00)
    formatted_total_charge = f"{total_charge:.2f}"
    formatted_total_amount_ordered_ever = f"{total_amount_ordered_ever:.2f}"
    request.session['last_quantity_ordered'] = quantity_from_form
    request.session['last_item_price'] = formatted_total_charge
    request.session['last_item_ordered'] = item_ordered.description
    request.session['total_quantity_ordered_ever'] = total_quantity_ordered_ever
    request.session['total_amount_ordered_ever'] = formatted_total_amount_ordered_ever
    return redirect("store:purchase_details")
def purchase_details(request):
    return render(request, "store/checkout.html")