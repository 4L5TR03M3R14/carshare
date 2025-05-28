from django.core.exceptions import PermissionDenied
from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, comment
from .forms import CommentForm

def index(request):
    context_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': context_list}
    return render(request, 'product/content_list.html',context)

    def detail(request, content_id):
     content_list = get_object_or_404(MainContent, pk=content_id)
     context = { 'content_list': content_list}
    return render(request, 'product/content_detail.html', context)
    @login_required(login_url='account:login')
    def comment_create(request, context_id):
        context_list = get_object_or_404(MainContent, pk=content_id)

if  request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_vaild():
        comment = form.save(commit=False)
        comment.content_list = context_list
        comment.author = request.user
        comment.save()
        return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()

        context = {'content_list': content_list, 'form': form}
        return render(request, 'product/content_detail.html', context)