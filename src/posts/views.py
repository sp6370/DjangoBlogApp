from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse


#no page error handle
def posts_list_view(request):
    return HttpResponse("Test")

# draft access error handle
def posts_detail_view(request, slug):
    return HttpResponse("Test")
    
@login_required
def posts_create_view(request):
    return HttpResponse("Test")

@login_required
def posts_update_view(request, slug):
    return HttpResponse("Test") 