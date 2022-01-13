from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import BlogPost
from django.contrib import messages
from .forms import BlogPostModelForm

#no page error handle
def posts_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def posts_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if(obj.status == "P"):
        template_name = 'detail.html'
        context = {"object": obj}
        return render(request, template_name, context) 
    if(obj.status == "D" and request.user == obj.user):
        template_name = 'detail.html'
        context = {"object": obj}
        return render(request, template_name, context)   
    else:
        template_name = 'detail.html'
        context = {"object": None}
        messages.error(request,"Unauthorized Access. If you are post author please login and retry.")
        return render(request, template_name, context) 

@login_required
def posts_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
        messages.info(request,"Post Successfully Created.")
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context) 

@login_required
def posts_update_view(request, slug):
    return HttpResponse("Test") 