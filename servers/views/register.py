
# Imports ###########################################################

from django.views.generic.edit import FormView
from servers.forms.users import UserCreateForm


# Views #############################################################

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = '/register/confirmation/'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
