from django.shortcuts import render , redirect
from .models import Feedback

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        value_suggest = Feedback()
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('contact') and request.POST.get('feed'):
            value_suggest.name = request.POST.get('name')
            value_suggest.email = request.POST.get('email')
            value_suggest.contact = request.POST.get('contact')
            value_suggest.feed = request.POST.get('feed')
            value_suggest.save()
            return redirect('submitted')
    else:
        return render(request , 'feedback.html')


def submited(request):
    return render(request , 'done.html')
