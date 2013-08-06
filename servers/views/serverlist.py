
# Imports ###########################################################

from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic.list import ListView

from servers.models.server import Server


# Views #############################################################

# TODO Permissions - only allow admins here

class ServerListView(ListView):
    model = get_user_model()
    template_name = 'servers/list.html'
    context_object_name = 'user_list'
    paginate_by = 100

    def post(self, request):
        user_pk = request.POST.get('user_pk')
        user = self.model.objects.get(pk=user_pk)
        server_pk = Server.objects.create_server(user)
        return redirect('server_detail', pk=server_pk)
