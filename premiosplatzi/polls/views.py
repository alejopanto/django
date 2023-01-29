from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Estas en la pagina principal")


def detail(request, question_id):
    return HttpResponse(f"estas viendo la pregunta numero {question_id}")


def results(request, question_id):
    return HttpResponse(f"estas viendo los reslutados de la pregunta numero {question_id}")


def vote(request, question_id):
    return HttpResponse(f"estas votando a la pregunta numero {question_id}")