
# Imports ###########################################################

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views.serverlist import ServerListView
from views.serverdetail import ServerDetailView
from views.register import RegisterView


# URLs ##############################################################

urlpatterns = patterns('',
    url(r'^$', RegisterView.as_view(), name=u'register'),
    url(r'^server/?$', ServerListView.as_view(), name=u'server_list'),
    url(r'^server/(?P<pk>\d)/?$', ServerDetailView.as_view(), name=u'server_detail'),
    url(r'^register/confirmation/?$', TemplateView.as_view(template_name=u'register_confirmation.html')),
)
