from django.forms import ModelForm
from .models import Item

# Create the form class.
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','time_added','picture']

        