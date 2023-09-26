from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from encuesta.models import Topic


def index(request):
    return render(request, 'index.html')


def categories(request):
    topics = Topic.objects.all()
    template = loader.get_template('categories.html')
    context = {
        'topics': topics,
    }
    return HttpResponse(template.render(context, request))


def category(request, id):
    topic = Topic.objects.filter(id=id).first()
    template = loader.get_template('category.html')
    context = {
        'topic': topic,
    }
    return HttpResponse(template.render(context, request))