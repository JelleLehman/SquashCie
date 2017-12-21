from django.http import HttpResponse
from django.template import loader
from .models import Match

def index(request):
    all_matches = Match.objects.all()
    template = loader.get_template('competition/Assignment 1/index.html')
    return HttpResponse(template.render(context, request))

def detail(request, match_id):
    return HttpResponse("<h2>Result</h2>")
