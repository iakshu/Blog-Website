from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Custom Validations
def ForbiddenUsers(value):
    forbidden_users = ['admin', 'authenticate', 'login', 'logout', 'administrator', 'root',
                        'email', 'user', 'sql', 'static', 'delete']
    if value.lower() in forbidden_users:
        raise ValidationError('Invalid name for user, this is a reserverd word. Try something else.')

def InvalidUser(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('This is an Invalid user, Do not use these chars: @, -, +')

# def UniqueEmail(value):
#     if User.objects.filter(email__iexact = value).exists():
#         raise ValidationError('Email already exists.')
#
# def UniqueUser(value):
#     if User.objects.filter(username__iexact = value).exists():
#         raise ValidationError('Username already exists.')

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 100, required = True)
    last_name = forms.CharField(max_length = 100, required = False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self.fields['username'].validators.append(ForbiddenUsers)
        self.fields['username'].validators.append(InvalidUser)
        # self.fields['username'].validators.append(UniqueUser)
        # self.fields['email'].validators.append(UniqueUser)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk = self.instance.pk).get(username = username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Username already exists.')