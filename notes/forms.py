from .models import NoteBoard
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = NoteBoard
        fields = ["note_title", "note_text", "note_tags"]
        widgets = {
            "note_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': r'Название'

            }),
            "note_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': r'Заметка'
            }),
            "note_tags": Textarea(attrs={
                'class': 'form-control',
                'placeholder': r'Тэги'
            }),
        }
