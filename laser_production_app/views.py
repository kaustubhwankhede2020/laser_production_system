from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Daily_update
import datetime
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def show_index_page(request):
    return render(request, 'index.html')

def submit_entry(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        employee_number = request.POST.get('employee_number')
        shift_code = request.POST.get('shift_code')
        component_type = request.POST.get('component_type')
        component_lk_number = request.POST.get('component_lk_number')
        component_lot_number = request.POST.get('component_lot_number')
        component_quantity = request.POST.get('component_quantity')
        try:
            Daily = Daily_update(date=datetime.datetime.now(),shift = shift_code, employee_number=employee_number,component_type=component_type,component_lk_number=component_lk_number,component_lot_number=component_lot_number,component_quantity=component_quantity,created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
            Daily.save()
            messages.success(request,'Entry Added Successfully')
            return HttpResponseRedirect(reverse("index"))

        except Exception as e:
            print(e)
            messages.error(request,'Failed to add entry')
            return HttpResponseRedirect(reverse("index"))
