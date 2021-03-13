from django.shortcuts import render
from .models import Main

# Create your views here.
# CRUD - create retrieve update delete (list)
# List all
def main_view(request):
    main_obj = Main.objects.all()
    context = {
        'main_obj': main_obj,
        'hello': 'hello world from context'
    }
    return render(request,"main/index.html",context)