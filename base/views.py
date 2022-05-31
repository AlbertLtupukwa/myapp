from django.contrib import messages
from django.shortcuts import render

from base.models import Message

# Create your views here.
def index(request):
    texts = Message.objects.all()
    if request.method == 'POST':
        message = Message.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            body=request.POST.get("body"),
        )
        messages.success(request, 'Message sent successfully')
    context = {'texts': texts}
    return render(request, 'base/index.html', context)