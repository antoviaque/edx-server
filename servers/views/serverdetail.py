
# Imports ###########################################################

from django.http import HttpResponseForbidden
from django.views.generic.detail import DetailView

from servers.models.server import Server


# Views #############################################################

class ServerDetailView(DetailView):
    model = Server
    template_name = 'servers/detail.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('servers.can_admin'):
            return HttpResponseForbidden()
        return super(ServerDetailView, self).dispatch(request, *args, **kwargs)
    
