from django.shortcuts import render

# Create your views here.
def show_index_page(request):
    return render(request, 'index.html')

def submit_entry(request):
    return render(request, 'index.html')