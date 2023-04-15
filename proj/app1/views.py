from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app1(request):
    template=loader.get_template('app1.html')
    return HttpResponse(template.render())