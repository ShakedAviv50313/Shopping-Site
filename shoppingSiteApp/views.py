from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item
from taggit.models import Tag
from django.db.models import Q

# Create your views here.


def index(request):
    items = Item.objects.order_by('-time_added')
    context = {'items': items}
    return render(request, 'shoppingSiteApp/index.html', context)


def tagged(request, tag, **kwargs):
    tag = get_object_or_404(Tag, name=tag)
    items = Item.objects.filter(Q(tags__name__icontains=tag))
    context = {'items': items}
    return render(request, 'shoppingSiteApp/index.html', context)
