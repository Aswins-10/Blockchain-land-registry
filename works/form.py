from django import forms
from .models import NewWorks, WorkExpenditure, Property


class NewWorksCreate(forms.ModelForm):
    class Meta:
        model = NewWorks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NewWorksCreate, self).__init__(*args, **kwargs)
        self.fields["District"].empty_label = "select"
        self.fields["District"].required = False


class NewExpenditureCreate(forms.ModelForm):
    class Meta:
        model = WorkExpenditure
        fields = '__all__'
        labels = {'ProjectName': 'Project Name', 'description': 'Description', 'exp': 'Expenditure'}

    def __init__(self, *args, **kwargs):
        super(NewExpenditureCreate, self).__init__(*args, **kwargs)
        self.fields["ProjectName"].empty_label = "select"
        self.fields["ProjectName"].required = False


class PropertyCreate(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['Owner', 'status','Tosell']

    def __init__(self, *args, **kwargs):
        super(PropertyCreate, self).__init__(*args, **kwargs)
        self.fields["District"].empty_label = "select"
        self.fields["District"].required = False


