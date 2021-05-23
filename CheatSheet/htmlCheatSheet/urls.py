from django.conf.urls import url, include
from django.contrib import admin
from htmlCheatSheet import views
urlpatterns = [
    url(r'^$', views.HtmlCheatPage.as_view(), name='htmlpage'),
]
