from django import forms
from django.forms import ModelForm, fields
from htmlCheatSheet.models import HtmlModel, CommentModel


class HtmlModelForm(ModelForm):

    class Meta:
        model = HtmlModel
        fields = ('title', 'description', 'example_html')


class CommentModelForm(ModelForm):

    class Meta:
        model = CommentModel
        fields = ('author', 'text')
