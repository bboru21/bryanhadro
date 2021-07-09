import re

from django import forms

from .models import (
    Artist,
)

class ArtistAdminForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(ArtistAdminForm, self).save(commit=False)

        # save sort_name as Beatles, The
        sort_name = self.cleaned_data.get('name')
        m = re.match('The ', sort_name)
        if m:
            sort_name = '{}, {}'.format(
                sort_name[m.end():],
                sort_name[m.start():m.end()-1],
            )
        instance.sort_name = sort_name

        if commit:
            instance.save()
            # self.save_m2m()
        return instance

    class Meta:
        model = Artist
        fields = ('name','sort_name',)
