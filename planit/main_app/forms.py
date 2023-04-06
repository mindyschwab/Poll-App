from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'choice_one', 'choice_two', 'choice_three']