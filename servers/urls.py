
# Imports ###########################################################

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views.register import RegisterView


# URLs ##############################################################

urlpatterns = patterns('',
    url(r'^$', RegisterView.as_view(), name=u'register'),
    url(r'^beta/confirmation$', TemplateView.as_view(template_name=u'beta_confirmation.html')),
)
