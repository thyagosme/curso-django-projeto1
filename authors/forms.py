from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing_attr =  field.widget.attrs.get(attr_name,'')
    field.widget.attrs[attr_name] = f'{existing_attr}{attr_new_val}'.strip()
    
def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        
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
