from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	url(r'^$', views.firstpage, name='firstpage'),
    url(r'^index/', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logoutt/', views.logout_view, name='logoutt'),
url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
