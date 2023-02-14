from ast import Delete
from multiprocessing import context
from re import template
from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpResponse
from . models import Item
from django.template import loader
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.core.exceptions import PermissionDenied

def edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied

# Create your views here.
 
'''def index(request):
    item_list =  Item.objects.all()
    context={
        'item_list':item_list,
        
     }
    return render(request,'food/index.html',context)

WE HAVE REPLACE THIS WITH IndexCassView.

'''

class IndexClassView(ListView):
    model = Item;
    template_name='food/index.html'
    context_object_name = 'item_list'





'''def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
           'item':item,
        }
    return render(request,'food/detail.html',context)
    
WE HAVE REPLACE THIS FUNCTION WITH FoodDetail CLASS.
'''


class FoodDetail(DetailView):
    model= Item
    template_name= 'food/detail.html'



'''@login_required
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})
    
THIS WAS REPLACE WITH CreateItem CLASS
'''

class CreateItem(CreateView):
    model= Item;
    fields = ['item_name','item_desc','recipe','item_image']
    template_name= 'food/item-form.html'



    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)
    
    


@login_required
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form,'item':item})

@login_required
def delete_item(request,id):
    item = Item.objects.get(id=id)

    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})
    
 