from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required
def comunicado(request):
    """ a view to show messages page"""
    forums = forum.objects.all()
    count = forums.count()
    discussions =[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {
        'forums': forums,
        'count': count,
        'discussions': discussions
    }

    return render(request, 'comunicado/comunicado.html', context)


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'comunicado/addInForum.html', context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'comunicado/addInDiscussion.html', context)
