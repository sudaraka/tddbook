""" List url definitions """

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'lists',
    url(r'^(\d+)/$', 'views.view_list', name='view_list'),
    url(r'^new$', 'views.new_list', name='new_list'),
)
