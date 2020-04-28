from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] # solo el 'text field'
        labels = {'test': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'} # a blank label
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
