# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
    template = loader.get_template('template.html')
    context = {    }
    return HttpResponse(template.render(context, request))
def translation(request):
    id = request.GET.get('id');
    context = {}
    template = loader.get_template('template.html')
    if id != None:
        r = requests.get('http://localhost:8983/solr/somali/select?q=id:"' + id + '"');
        response = r.json();

        if len(response['response']['docs']) >= 1:
            context = {"en":response['response']['docs'][0]['en'][0],
                       "so": response['response']['docs'][0]['so'][0],
                       "id": response['response']['docs'][0]['id']}
        else:
            context = {"error": "No word found for this ID"}
    return HttpResponse(template.render(context, request))


