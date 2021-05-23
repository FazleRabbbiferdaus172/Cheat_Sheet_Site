from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    return render(request, 'base.html')


class HtmlCheatPage(TemplateView):
    template_name = 'htmlCheatSheet/htmlCheatPage.html'
