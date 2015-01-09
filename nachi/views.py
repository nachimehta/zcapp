from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import logging

from nachi.models import *

def index(request):

    return render(request, 'nachi/customer.html', {'customer': 1})

def customer(request):

	menus = Menu.objects.all()

	menu_type = 'Dinner'

	entrees = Entree.objects.filter(menu__name = menu_type) #default to dinner

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

@csrf_exempt
def change_menu(request):

	if request.method == 'POST':
		entrees = Entree.objects.filter(menu__name = request.POST['menu_type'])

		return HttpResponse(serializers.serialize('json', entrees), content_type='application/json')