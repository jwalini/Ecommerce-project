
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User,Address
from store.models import Product,Order,OrderItem

USER_ID = 5 
#user starts from '5', others deleted
def get_common_user():
    
    try:
        return User.objects.get(id=USER_ID)
    except User.DoesNotExist:
        return None



def home(request):
    context={}
    SearchKey = request.GET.get('SearchKey','')
    if SearchKey:
        all_products = Product.objects.filter(title__contains=SearchKey)
    else:
        all_products = Product.objects.all()
    
    if all_products:
        context = {'all_products':all_products}
    else:
        context = {'msg':'Product Not available!!'}
    
    context['user'] = get_common_user()
 
    return render(request, 'home.html', context)
    


def profile(request,id):
    context={}
    user = get_common_user()
    if not user:
        return HttpResponse('User Not Found', status=404)

    order = Order.objects.filter(user=user).order_by('-created_at').first()
    order_items = OrderItem.objects.filter(order=order) if order else []

    context = {
        'user': user,
        'order': order,
        'order_items': order_items
    }
    return render(request, 'profile.html', context)


def delete_book(request,id):
    context={}
    try:
        orderitem = OrderItem.objects.get(id=id)
    except:
        return HttpResponse('404 : Product Not Found')
    
    context['orderitem']=orderitem
    if request.method == 'POST':
        orderitem.delete()
        return redirect('home')
    return render(request, 'delete_confirm.html', context)