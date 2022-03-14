import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing_attr =  field.widget.attrs.get(attr_name,'')
    field.widget.attrs[attr_name] = f'{existing_attr}{attr_new_val}'.strip()
    
def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder',placeholder_val)
    
    
def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='invalid'
        )

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_attr(self.fields['username'], 'css', 'a-css-class')
        
    password = forms.CharField( 
                required = True,
                widget= forms.PasswordInput(attrs = {
                    'placeholder': 'Repeat your password'
    
                }),
                error_messages= {
                    'required': 'Password must not be empty.'
                },
                help_text = ('Passowrd must have at least one uppercase letter, '
                             'one lowercase letter and one number.'
                             'The length should be at least 8 characters.'),
                validators=[strong_password],
             
                
            )
    
    password2 = forms.CharField( 
                required = True,
                widget= forms.PasswordInput(attrs = {
                    'placeholder': 'Repeat your password'
    
                }),
                   label= ('Password confirmation')
            )
    class Meta:
        model =  User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            
        ]
        #exclude =[]
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'E-mail',
            'password':  'Password',
            }
        help_texts = {
            'email': 'The e-mail might be valid.'
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty.'
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs = {
                'placeholder': 'Type your first name here.',
                'class': 'classe-1 classe-2'
                }),
            'password': forms.PasswordInput(attrs = {
                'placeholder': 'Type your password here.'
            })
            
        }
    def clean_password(self):
        data = self.cleaned_data.get('password')
        if 'atenção' in data:
            raise ValidationError(
                'Do not type %(value)s in password field.',
                code =  'invalid',
                params = {'value': 'atenção'}
            )
            
        return data  
    
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo first name',
                code='invalid',
                params={'value': '"John Doe"'}
            )

        return data
    
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error, 
                    'Another error'
                ],  
            })
