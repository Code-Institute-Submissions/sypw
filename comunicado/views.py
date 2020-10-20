from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Forum, Discussion
from profiles.models import UserProfile

from django.contrib import messages
from .forms import CreateInDiscussion, CreateInForum


@login_required
def comunicado(request):
    """ a view to show messages page"""
    forums = Forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {
        'forums': forums,
        'count': count,
        'discussions': discussions
    }

    return render(request, 'comunicado/comunicado.html', context)


def addInForum(request):
    name = get_object_or_404(UserProfile, user=request.user)
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        # name = get_object_or_404(UserProfile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('comunicado'))
    context = {
        'form': form,
        'name': name,
        }
    return render(request, 'comunicado/addInForum.html', context)


def addInDiscussion(request):
    nick = get_object_or_404(UserProfile, user=request.user)
    forum = Forum.topic
    form = CreateInDiscussion(initial={'forum': forum, 'nick': nick})
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        nick = get_object_or_404(UserProfile, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('comunicado')
    context = {
        'forum': forum,
        'form': form,
        'nick': nick,
    }
    return render(request, 'comunicado/addInDiscussion.html', context)


# def editInForum(request, forum_id):
#     "Edit the Forum"
#     forum = get_object_or_404(Forum, pk=forum_id)
#     form = CreateInForum(instance=forum)
#     messages.info(request, f'You are editing {forum.topic}')
#     # topic = forum.topic
#     # description = forum.description

#     template = 'comunicado/editInForum.html'
#     context = {
#         'form': form,
#         # {
#         #     'topic': topic,
#         #     'description': description,
#         # },
#         'forum': Forum,
#     }

#     return render(request, template, context)


def editInDiscussion(request, discussion_id):
    """Editing a discusion """
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    # nick = Discussion.nick
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST, request.FILES, instance=discussion)
        if form.is_valid:
            form.save()
            messages.success(request, "Great, you fixed that!")
            return redirect(reverse('comunicado'))
        else:
            messages.error(request, "Failed to update that. Please ensure the form is valid.")
    else:
        form = CreateInDiscussion(instance=discussion)
        messages.info(request, f'you can now edit {Discussion.nick} opinion')

    template = 'comunicado/editInDiscussion.html'
    context = {
        'form': form,
        'discussion': discussion,
        # 'nick': nick
    }

    return render(request, template, context)


def deleteInForum(request, forum_id):
    """ Delete whole forum"""
    forum = get_object_or_404(Forum, pk=forum_id)
    forum.delete()
    messages.success(request, "Forum deleted successfuly!")
    return redirect(reverse('comunicado'))


def deleteInDiscussion(request, discussion_id):
    """ Delete whole forum"""
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    discussion.delete()
    messages.success(request, "Answer deleted successfuly!")
    return redirect(reverse('comunicado'))
