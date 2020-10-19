from django.shortcuts import render, get_object_or_404

from django.forms import ModelForm
from .models import Forum, Discussion
from profiles.models import UserProfile


class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        # name = Forum.name
        super().__init__(*args, **kwargs)
        placeholders = {
            # 'name': 'Your Name',
            'email': 'Email Address',
            'topic': 'New subject',
            'description': 'Here you can describe your idea',
        }

        self.fields['topic'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'name':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        forum = Forum.topic
        nick = UserProfile.user
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'forum': 'Choose Forum',
            'discuss': 'Your message',
        }

        self.fields['discuss'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'nick':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
