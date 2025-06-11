from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Программно задаем заглавные буквы у заголовков полей
        for field_name, field in self.fields.items():
            if field.label:
                field.label = str(field.label).capitalize()

    class Meta:
        model = Feedback
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': _('Enter subject')}),
            'message': forms.Textarea(attrs={'class': 'form-control mt-2', 'placeholder': _('Enter your message'), 'rows': 5}),
        }
        labels = {
            'subject': _('subject'),
            'message': _('message'),
        }
        help_texts = {}
