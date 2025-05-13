from django.shortcuts import render
from .models import MainContent

def index(request):
    context_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': context_list}
    return render(request, 'product/content_list.html',context)

