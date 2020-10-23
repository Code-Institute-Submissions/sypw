from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Forum, Discussion
# from profiles.models import UserProfile
# from django.contrib.auth.models import User

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

    forum = get_object_or_404(Forum, pk=forum_id)
    form = CreateInDiscussion(request.POST, request.FILES, initial={'forum': forum, 'nick': nick})
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST, request.FILES, initial={'forum': forum, 'nick': nick})

        if form.is_valid():
            form = form.save(commit=False)
            form.nick = nick
            form.email = email2
            form.forum = forum
            form.save()
            return redirect('comunicado')
        else:
            print("iiiiiiiiiiooooooooooooooooooo iiiiiiiiiioooooooooooo this is django police. Your form is invalid bro!")

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
# discussion = get_object_or_404(Discussion, pk=discussion_id)
    user = request.user
    author = discussion.nick
    if user == author:
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
    else:
        messages.error(request, "You cannot edit this message, because it's not yours!")
        print("You were trying to edit the post of other author, you naughty naughty!")
        placeholder = "You cannot edit this message, because it's not yours!"
        form = CreateInDiscussion(request.POST, initial={'forum': discussion, 'nick': user, 'discuss': placeholder })

    # if request.method == 'POST':
    #     form = CreateInDiscussion(request.POST, request.FILES, instance=discussion)
    #     if form.is_valid:
    #         form.save()
    #         messages.success(request, "Great, you fixed that!")
    #         return redirect(reverse('comunicado'))
    #     else:
    #         messages.error(request, "Failed to update that. Please ensure the form is valid.")
    # else:
    #     form = CreateInDiscussion(instance=discussion)
    #     messages.info(request, f'you can now edit {Discussion.nick} opinion')

    template = 'comunicado/editInDiscussion.html'

    context = {
        'form': form,
        'discussion': discussion,
        # 'nick': nick
    }

    return render(request, template, context)


def deleteInForum(request, forum_id):
    """ Delete whole forum"""
    user = request.user
    forum = get_object_or_404(Forum, pk=forum_id)
    author = forum.name
    print(f'This is the author of that forum topic: {author}')
    if user == author:
        forum.delete()
    else:
        messages.error(request, "You cannot delete this topic.")
        print("You were trying to delete the form of other author, you naughty naughty!")
    # forum.delete()
    messages.success(request, "Forum deleted successfuly!")
    return redirect(reverse('comunicado'))


def deleteInDiscussion(request, discussion_id):
    """ Delete whole forum"""
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    user = request.user
    author = discussion.nick
    if user == author:
        discussion.delete()
    else:
        messages.error(request, "You cannot delete this topic.")
        print("You were trying to delete the post of other author, you naughty naughty!")
    # discussion.delete()
    messages.success(request, "Answer deleted successfuly!")
    return redirect(reverse('comunicado'))
