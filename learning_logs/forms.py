from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.TextInput(attrs={'class':'form-control'})}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name','text']
        labels = {'name':'Название','text': 'Пишите здесь'}
        widgets = {'text':forms.Textarea(attrs={'cols':80,'class':'form-control'}),
                   'name':forms.TextInput(attrs={'class':'form-control'})}