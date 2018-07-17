from django.shortcuts import render

from .models import AddGoods, Clerk, Counter


# Create your views here.
def index(request):
    goods_list = AddGoods.objects.all()
    return render(request, 'jubo_shop/index.html', {
        'goods_list': goods_list,
    })
