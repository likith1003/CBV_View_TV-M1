from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from .forms import *
# Create your views here.


def fbv_string(request):
    if request.method == "POST":
        return HttpResponse('Welcome to fbv_string page')

class Cbv_String(View):
    def get(self, request):
        return HttpResponse('Welcome to Cbv_String Page')
    
    def post(self, request):
        return HttpResponse('Welcomew to POSt method of CBV')
    

def insert_school_by_fbv(request):
    ESFO = SchoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_school_by_fbv.html', d)


class insert_school_by_cbv(View):
    def get(self, request):
        ESFO = SchoolForm()
        d = {'ESFO': ESFO}
        return render(request, 'insert_school_by_cbv.html', d)
    
    def post(self, request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        return HttpResponse('Invalid Data')
    

class TV(TemplateView):
    template_name='TV.html'