from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):

    def clean(self):
        data = self.cleaned_data

        name = data.get('comment_title')
        email = data.get('comment_email')
        comment = data.get('comment')

        if len(name) < 5:
            self.add_error(
                'comment_title',
                'Nome precisa ter mais que 5 caracteres'
            )

    class Meta:
        model = Comment
        fields = ('comment_title', 'comment_email', 'comment',)
