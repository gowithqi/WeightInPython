from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<poll_id>\d+)/votes/$', views.vote, name='vote')
)

