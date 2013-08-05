
# Imports ###########################################################

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views.create import CreateView
from views.register import RegisterView


# URLs ##############################################################

urlpatterns = patterns('',
    url(r'^$', RegisterView.as_view(), name=u'register'),
    url(r'^create/?$', CreateView.as_view(), name=u'create'),
    url(r'^register/confirmation/?$', TemplateView.as_view(template_name=u'register_confirmation.html')),
)
