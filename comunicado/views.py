from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Forum, Discussion
from profiles.models import UserProfile
from django.contrib.auth.models import User

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
    name = request.user

    # print(f"User's name: {name} and type {type(name)}")
    form = CreateInForum(initial={'name': name})

    if request.method == 'POST':
        form = CreateInForum(request.POST)
        # name = get_object_or_404(UserProfile, user=request.user)
        if form.is_valid():
            forum_form = form.save(commit=False)
            forum_form.name = name
            forum_form.save()
            return redirect(reverse('comunicado'))

    # form = CreateInForum(instance=profile)
    context = {
        'form': form,
        'name': name,
        }

    return render(request, 'comunicado/addInForum.html', context)


def addInDiscussion(request, forum_id):
    nick = request.user
    email2 = request.user.email
    print(f"oooooooooooooooooooooooooo The form with email: {email2}")
    # forum = Forum.topic

    forum = get_object_or_404(Forum, pk=forum_id)
    print(f"aaaaaaaaaaaaaaaaaaaaaaaaa The form with FORUM: {forum}")

    
    # def form_valid(self, form):
    #     if self.request.POST.get('parent'):
    #         forum.parent_id = self.request.POST.get('parent')
    #         forum.save()

    form = CreateInDiscussion(request.POST, request.FILES, instance=forum, initial={'forum': forum, 'nick': nick})
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST, request.FILES, instance=forum, initial={'nick': nick})
        print(f"bbbbbbbbbbbbbbbbbbbbbbbbbb Forum {forum}")
        # nick = get_object_or_404(UserProfile, user=request.user)

        if form.is_valid():
            print(f"cccccccccccccccccccccccccccccccccccccc Forum {forum}")
            form = form.save(commit=False)
            form.nick = nick
            form.email = email2
            form.forum = forum
            form.save()
            return redirect('comunicado')

    # template = redirect(reverse('addInDiscussion', forum_id))
    template = 'comunicado/addInDiscussion.html'
    context = {
        'forum_id': forum.id,
        'forum': forum,
        'form': form,
        'nick': nick,
    }

    return render(request, template, context,)


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
