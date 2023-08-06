from django.shortcuts import render, redirect, HttpResponse
from .models import Form

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        
        msg = Form.objects.create(name=name,email=email,message=message)
        msg.save();
        
        return redirect('success')
        
    else:
        return render(request, 'home.html')


def news(request):
    return render(request, 'news-detail.html')

def success(request):
    return render(request, 'success.html')