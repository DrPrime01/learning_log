from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Entry, Topic
from .forms import TopicForm, EntryForm

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

def new_topic(request, *args, **kwargs):
    """Page for adding new topics"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, "new_topic.html", context)

def new_entry(request, topic_id, *args, **kwargs):
    """Page for writing new topics entries"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid:
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, "new_entry.html", context)

def edit_entry(request, entry_id, *args, **kwargs):
    """A Page for editing entries"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'form': form, 'entry': entry, 'topic':topic}
    return render(request, "edit_entry.html", context)
        