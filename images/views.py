from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html", {"image":image})