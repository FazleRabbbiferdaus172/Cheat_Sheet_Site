from htmlCheatSheet.forms import CommentModelForm
from django.contrib import admin
from htmlCheatSheet.models import HtmlModel, CommentModel
# Register your models here.
admin.site.register(HtmlModel)
admin.site.register(CommentModel)
