from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics.order_by('-count_entries')}
    return render(request, 'learning_logs/topics.html', context=context)


def entries(request, name):
    topic = Topic.objects.get(text=name)
    context = {'topic': topic.text, 'entries': topic.entry_set.order_by('date_added')}
    return render(request, 'learning_logs/entries.html', context=context)


@login_required
def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись
        form = TopicForm()
    else:
        # Данные отправлены
        form = TopicForm(data=request.POST)
        if form.is_valid():
            nt = form.save(commit=False)
            nt.owner = request.user
            nt.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, name):
    topic = Topic.objects.get(text=name)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            topic.count_entries += 1
            topic.save()
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:entries', args=[name, ]))
    context = {'form': form, 'topic': topic.text}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, name, entry_id):
    topic = Topic.objects.get(text=name)
    entry = topic.entry_set.get(id=entry_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            edit_entry = form.save(commit=False)
            edit_entry.topic = topic
            edit_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:entries', args=[name, ]))
    context = {'form': form, 'topic': topic.text, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)
