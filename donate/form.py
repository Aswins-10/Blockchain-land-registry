from django import forms
from .models import Donate


class NewDonationCreate(forms.ModelForm):
    class Meta:
        model = Donate
        fields = '__all__'
        fields = ['projectname', 'amount', 'remarks', ]
        labels = {'projectname': 'Select Project', 'amount': 'Amount', 'remarks': 'Remarks'}
        # help_text = {'received': 'Select Receiver'}
        # # received.widget.attrs['required']
        # error_messages = {'projectname': {'required': 'Receiver required'}}

    def __init__(self, *args, **kwargs):
        super(NewDonationCreate, self).__init__(*args, **kwargs)
        self.fields["projectname"].empty_label = "select"
        self.fields["projectname"].required = True
        # self.fields["username"].empty_label = "select"
        # self.fields["username"].required = True

    # widgets = {'filename': forms.FileField}
