from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .upload import load_file
from .forms import UploadFileForm



def index(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(reverse('visualization:index'))
    else:
        form = UploadFileForm()

    return render(request, 'visualization/index.html', {'form':form})
