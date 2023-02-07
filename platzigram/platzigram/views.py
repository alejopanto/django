# Django
from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json


def hello_world(request):
    # Return a greeting
    return HttpResponse('Hello, world!, la hora es {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    # Retunr a list int sorted
    #import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    # return HttpResponse(
    #     json.dumps(data, indent=4),
    #     content_type='application/json'
    # )
    return JsonResponse(data)


def say_hi(request, name, age):
    #return a greeting
    if age < 12:
        message = f'sorry {name}, your age is {age}, you are not allowed'
    else:
        message = f'Hello, {name}! your age is {age}, welcome to platzigram'

    return HttpResponse(message)