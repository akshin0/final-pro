from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event, Program
from .forms import SubscriberForm

# Create your views here.
def index(request):
    context = {'events': Event.objects.all(), 'programs':Program.objects.all()}
    return render(request, "index.html", context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Subscribed!')
            return redirect('home')
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})
