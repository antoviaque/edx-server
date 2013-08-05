
# Imports ###########################################################

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


# Views #############################################################

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/register/confirmation/'
