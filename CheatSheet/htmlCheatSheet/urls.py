from django.conf.urls import url, include
from django.contrib import admin
from htmlCheatSheet import views
urlpatterns = [
    url(r'^$', views.HtmlCheatPage.as_view(), name='htmlpage'),
    url(r'^new/', views.CreateHtmlModelView.as_view(), name="post_new"),
    url(r'^list', views.HtmlModelListView.as_view(), name='htmllist'),
]
