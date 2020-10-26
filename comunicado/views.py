from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Forum, Discussion

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


def add_in_forum(request):
    name = request.user
    email2 = request.user.email
    form = CreateInForum(initial={'name': name})

    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            forum_form = form.save(commit=False)
            forum_form.name = name
            forum_form.email = email2

            forum_form.save()
            return redirect(reverse('comunicado'))

    context = {
        'form': form,
        'name': name,
        }

    return render(request, 'comunicado/add_in_forum.html', context)


def add_in_discussion(request, forum_id):
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
            messages.info(request, f'Your opinion has been added')
            return redirect('comunicado')
        else:
            print("iiiiiiiiiiooooooooooooooooooo iiiiiiiiiioooooooooooo this is django police. Your form is invalid bro!")

    template = 'comunicado/add_in_discussion.html'
    context = {
        'forum_id': forum.id,
        'forum': forum,
        'form': form,
        'nick': nick,
    }

    return render(request, template, context,)


# def edit_in_forum(request, forum_id):
#     """Edit the Forum"""
#     forum = get_object_or_404(Forum, pk=forum_id)
#     form = CreateInForum(request.POST, request.FILES, instance=forum)

#     messages.info(request, f'You are editing {forum.topic}')
#     topic = forum.topic
#     description = forum.description

#     if request.method == 'POST':
#         form = CreateInForum(request.POST, request.FILES, instance=forum)
#         if form.is_valid:
#             form.save()
#             messages.success(request, "You successfully updated that topic!")
#             return redirect(reverse('comunicado'))
#         else:
#             messages.error(request, "Failed to update that. Please ensure the form is valid.")
#     else:
#         form = CreateInDiscussion(instance=forum)
#         messages.info(request, f'you can now edit this topic')

#     template = 'comunicado/edit_in_forum.html'

#     context = {
#         'form': form,
#         'topic': topic,
#         'description': description,
#         'forum': forum,
#     }

#     return render(request, template, context)


def edit_in_discussion(request, discussion_id):
    """Editing a discusion """
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    user = request.user

    # Code underneath only allows users to edit their own message
    # In order to edit someone else's message, please see note below
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
            messages.info(request, f'you can now edit {author} opinion')
    else:
        messages.error(request, "You cannot edit this message, because it's not yours!")
        print("You were trying to edit the post of other author, you naughty naughty!")
        placeholder = "You cannot edit this message, because it's not yours!"
        form = CreateInDiscussion(request.POST, initial={'forum': discussion, 'nick': user, 'discuss': placeholder })

        """
        PLEASE READ: The commented code underneath is left in a purpose,
        as it will allow superuser to edit any message, despite the author,
        if we will comment whole that bit above and uncomment this one here.
        """
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
    #     messages.info(request, f'you can now edit {user} opinion')

    template = 'comunicado/edit_in_discussion.html'

    context = {
        'form': form,
        'discussion': discussion,
    }

    return render(request, template, context)


def delete_in_forum(request, forum_id):
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
        # Right now user can only delete the topic opened by themselves. 
        # If it will be neccesssary to delete other users topic, please uncomment function underneath
    # forum.delete()
    messages.success(request, "Forum deleted successfuly!")
    return redirect(reverse('comunicado'))


def delete_in_discussion(request, discussion_id):
    """ Delete your message"""
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    user = request.user
    author = discussion.nick
    if user == author:
        discussion.delete()
    else:
        messages.error(request, "You cannot delete this message.")
        print("You were trying to delete the post of other author, please don't do that!")
        # Right now users can only delete the messages wrote by themselves. 
        # If it will be neccesssary to delete other users message, please uncomment function underneath
    # discussion.delete()
    messages.success(request, "Message deleted successfuly!")
    return redirect(reverse('comunicado'))
