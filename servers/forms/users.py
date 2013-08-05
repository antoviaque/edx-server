
# Import ############################################################

from django.contrib.auth import get_user_model
from django import forms


# Classes ###########################################################

class UserCreateForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    email.
    """

    error_messages = {
        'duplicate_username': "A user with that username already exists.",
        'duplicate_email': "An user with that email already exists.",
    }
    username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w\d]+$',
        help_text="Required. 30 characters or fewer. Letters and digits only.",
        error_messages={'invalid': "This value may contain only letters and numbers."})
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ( "username", "email" )

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model()._default_manager.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        print user, commit
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control input-medium'
        self.fields['username'].widget.attrs['placeholder'] = 'myschool'
        self.fields['email'].widget.attrs['placeholder'] = 'bob@gmail.com'
