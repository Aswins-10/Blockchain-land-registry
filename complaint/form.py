from django import forms

from complaint.models import Complaint


class ComplaintCreate(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['projectname','subject', 'complainttext',  'upload']
        labels = {'projectname': 'Project Name', 'subject': 'Subject', 'complainttext': 'Complaint Dtls',
                  'upload': 'Upload File'}

    def __init__(self, *args, **kwargs):
        super(ComplaintCreate, self).__init__(*args, **kwargs)
        self.fields["projectname"].empty_label = "select"
        self.fields["projectname"].required = False


