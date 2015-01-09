from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import logging

from nachi.models import *

def index(request):
    return render(request, 'nachi/customer.html', {'customer': 1})

def customer(request):
	menus = Menu.objects.all()

	menu_type = 'Dinner'

	if request.method == 'POST':
		menu_type = request.POST.get('menu', 'Dinner');

	entrees = Entree.objects.filter(menu__name = menu_type)

	return render(request, 'nachi/customer.html', {'customer': 1, 'menus': menus, 'entrees': entrees, 'menu_type': menu_type})

def kitchen(request):
	orders = Order.objects.all()

	return render(request, 'nachi/kitchen.html', {'kitchen': 1, 'orders': orders})

def place_order(request):

	if request.method == 'POST':
		entrees = request.POST.getlist('entrees')
		order = Order(table_number = int(request.POST['table_number']))
		order.save()
		for entree in entrees:
			e = Entree.objects.get(name=entree)
			order.entrees.add(e)

	return redirect('/customer')

@csrf_exempt
def delete_order(request):

	if request.method == 'POST':
		o = Order.objects.get(pk=request.POST['orderId'])
		o.delete()

	return redirect('/kitchen')