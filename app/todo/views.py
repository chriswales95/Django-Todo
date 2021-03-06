from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect


def index(request):

    latest_items = Item.objects.all()[:10]
    template = loader.get_template('todo/index.html')
    context = {
        'latest_items': latest_items,
    }
    
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/accounts/login')


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    template = loader.get_template('todo/detail.html')
    context = {
        'item': item,
    }
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/accounts/login')


def new_item(request):
    template = loader.get_template('todo/new_item.html')

    if request.user.is_authenticated:
        return render(request, 'todo/new_item.html')
    else:
        return HttpResponseRedirect('/accounts/login')


def submit_new_item(request):
    if request.method == 'POST':
        a = Item(item=request.POST['item'], date=request.POST['date'],
                 priority=request.POST['priority'])
        a.save()
        return HttpResponseRedirect('/', request)
    else:
        return HttpResponseRedirect('/')

def completed_task(request, item_id):
    item = get_object_or_404(Item,pk=item_id)
    item.complete = True
    item.save()
    return HttpResponseRedirect('/')

def uncomplete_task(request, item_id):
    item = get_object_or_404(Item,pk=item_id)
    item.complete = False
    item.save()
    return HttpResponseRedirect('/completed/')

def completed(request):
    items = Item.objects.filter(complete=True)
    template = loader.get_template('todo/completed.html')
    context = {
        'items': items,
    }
    
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/accounts/login')

def all_items(request):
    items = Item.objects.all()
    context = { 'items': items,
    }
    template = loader.get_template('todo/all_items.html')
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/accounts/login')