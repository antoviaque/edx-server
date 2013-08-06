
# Imports ###########################################################

from django.views.generic.detail import DetailView

from servers.models.server import Server


# Views #############################################################

# TODO Permissions - only allow admins here

class ServerDetailView(DetailView):
    model = Server
    template_name = 'servers/detail.html'
