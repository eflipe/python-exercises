from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, 'learning_log/index.html')


@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data enviado; crea un blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            return redirect('learnings_app:topics')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learnings_app:topic', topic_id=topic_id)

    context = {'topic': topic,
               'form': form}

    return render(request, 'learning_log/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learnings_app:topic', topic_id=topic.id)

    context = {'entry': entry,
               'topic': topic,
               'form': form}

    return render(request, 'learning_log/edit_entry.html', context)
