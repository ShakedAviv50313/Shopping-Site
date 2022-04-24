from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.


def index(request):
    items = Item.objects.order_by('-time_added')
    context = {'items': items}
    return render(request, 'shoppingSiteApp/index.html', context)
