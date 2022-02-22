from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

from .models import Data


def index(request,ip):
    rq = requests.get(f"http://ip-api.com/json/{ip}").json()
    rq['as_query'] = rq['as']
    rq.pop('as')
    data = Data(**rq)
    data.save()
    rq = json.dumps(rq)
    return HttpResponse(rq)