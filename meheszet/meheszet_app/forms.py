from django.forms import  ModelForm
from .models import AddUser


class NatureOfBeekeeping(ModelForm):
    class Meta:
        model = AddUser
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['beekepingNature'].widget.attrs.update({
            'class': 'from-control',
        })
