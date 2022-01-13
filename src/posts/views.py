from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .models import BlogPost


#no page error handle
def posts_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

# draft access error handle
def posts_detail_view(request, slug):
    return HttpResponse("Test")
    
@login_required
def posts_create_view(request):
    return HttpResponse("Test")

@login_required
def posts_update_view(request, slug):
    return HttpResponse("Test") 