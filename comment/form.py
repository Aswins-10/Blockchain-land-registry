from django import forms

from comment.models import Comment



class CommentCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['projectname', 'commenttext',]
        labels = {'projectname': 'Project Name', 'commenttext': 'Comment Dtls'}

    def __init__(self, *args, **kwargs):
        super(CommentCreate, self).__init__(*args, **kwargs)
        self.fields["projectname"].empty_label = "select"
        self.fields["projectname"].required = True


