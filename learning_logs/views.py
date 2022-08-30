from django.shortcuts import render
#from django.http import HttpResponse
from .models import Topic

# Create your views here.

def homepage(request, *args, **kwargs):
    """A sample home page"""
    return render(request, "index.html", {})

def about(request, *args, **kwargs):
    """The about page"""
    return render(request, "about.html", {})

def topics(request, *args, **kwargs):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render (request, "topics.html", context)

def topic(request, topic_id, *args, **kwargs):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, "topic.html", context)