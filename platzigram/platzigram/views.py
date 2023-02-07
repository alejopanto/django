# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

def hello_world(request):
    # Return a greeting
    return HttpResponse('Hello, world!, la hora es {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    # HI
    #import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))