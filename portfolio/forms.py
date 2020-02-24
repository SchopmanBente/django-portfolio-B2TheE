from django import forms
from .models import *


class GraphicForm(forms.ModelForm):

        name = models.CharField()
        image = models.ImageField(upload_to='images')

        class Meta:
            model = Graphic
            fields = ('name', 'image',)