from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def index(request):

    latest_items = Item.objects.all()
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
        return HttpResponse(template.render())
    else:
        return HttpResponseRedirect('/accounts/login')
