from django.shortcuts import render
from django.views.generic import (
    TemplateView, CreateView, ListView, DetailView)
from htmlCheatSheet.models import HtmlModel
from htmlCheatSheet.forms import HtmlModelForm
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


class HtmlModelDetailView(DetailView):
    model = HtmlModel
    template_name = 'htmlCheatSheet/htmlCheatPagedetail.html'
