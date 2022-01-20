from django.forms import ModelForm
from .models import DjangoClasses


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'