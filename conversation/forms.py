from django import forms
from .models import ConversationMessage



class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class':' w-100 p-6 rounded-lg border',
                'placeholder':'Type your message here...', 
                'style':'height:100px'
            })
        }