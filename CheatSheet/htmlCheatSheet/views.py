from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView, CreateView, ListView, DetailView)
from htmlCheatSheet.models import HtmlModel
from htmlCheatSheet.forms import HtmlModelForm, CommentModelForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.http import HttpResponseForbidden
# Create your views here.


def index(request):
    return render(request, 'base.html')


class HtmlCheatPage(TemplateView):
    template_name = 'htmlCheatSheet/htmlCheatPage.html'


class HtmlModelListView(ListView):
    model = HtmlModel
    template_name = 'htmlCheatSheet/htmlCheatPageList.html'


class CreateHtmlModelView(CreateView):
    form_class = HtmlModelForm
    model = HtmlModel
    template_name = 'htmlCheatSheet/htmlmodel_form.html'


class HtmlModelDetailView(FormMixin, DetailView):
    model = HtmlModel
    form_class = CommentModelForm
    template_name = 'htmlCheatSheet/htmlCheatPagedetail.html'

    def get_success_url(self):
        return reverse('htmlCheatSheet:cheat_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        html = get_object_or_404(HtmlModel, pk=self.object.pk)
        comment = form.save(commit=False)
        comment.html = html
        comment.save()
        return super().form_valid(form)
