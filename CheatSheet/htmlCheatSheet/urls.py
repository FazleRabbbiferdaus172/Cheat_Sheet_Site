from django.conf.urls import url, include
from django.contrib import admin
from htmlCheatSheet import views
app_name = 'htmlCheatSheet'
urlpatterns = [
    url(r'^$', views.HtmlCheatPage.as_view(), name='htmlpage'),
    url(r'^new/', views.CreateHtmlModelView.as_view(), name="post_new"),
    url(r'^list', views.HtmlModelListView.as_view(), name='htmllist'),
    url(r'^cheat/(?P<pk>\d+)$',
        views.HtmlModelDetailView.as_view(), name='cheat_detail'),
    url(r'^cheat/(?P<pk>\d+)/edit/$',
        views.HtmlModelUpdateView.as_view(), name='cheat_edit'),
    url(r'^cheat/(?P<pk>\d+)/delete/$',
        views.HtmlModelDeleteView.as_view(), name='cheat_delete'),
]
