from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'third_task/platform_main.html')

def sail(request):
    return render(request, 'third_task/sail.html')

def contacts(request):
    return render(request, 'third_task/contacts.html')