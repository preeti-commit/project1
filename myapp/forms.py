from django import forms

from myapp.models import (World)


class SetLocationsForm(forms.ModelForm):
    class Meta:
        model = World
        fields = ('name','address','city','state','location')

    def save(self, commit=True):
        world = super().save(commit=False)
        world.is_location = True
        if commit:
            world.save()
        return world


