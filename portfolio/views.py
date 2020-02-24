from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def graphic_view(request):
    if request.method == 'POST':
        form = GraphicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = GraphicForm()
    return render(request, 'graphic.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')