from django.shortcuts import render
from django.views.generic import ListView


# class IndexListView(ListView):
#     model =


def index(request):
    return render(request, 'mail_service/index.html')
