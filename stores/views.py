from django.shortcuts import render, get_list_or_404
from .models import Store

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

from django.shortcuts import render, get_list_or_404

def store_detail(request, store_id):
    store = get_list_or_404(Store, id=store_id)
    context = {
        "store": store
    }
    return render (request, 'store_detail.html', context)
    

