
# Imports ###########################################################

from django.views.generic.base import TemplateView

from servers.tasks.openstack import nova_boot


# Views #############################################################

class CreateView(TemplateView):
    template_name = 'create.html'

    def get(self, request):
        task = nova_boot.apply_async(('arg1', 'arg2'))
        task_result = task.get(timeout=60)
        
        return self.render_to_response({
            'task_result': task_result,
        })
