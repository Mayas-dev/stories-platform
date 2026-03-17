from django.forms import ModelForm
from .models import Story
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StoryForm(ModelForm):
    class Meta:
        model=Story
        fields = ['name', 'content', 'genre', 'audience', 'format_type', 'perspective']
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']