from django import forms
from .models import Product, Category, Subcategory
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'sku', 'name', 'slug',
                  'description', 'has_sizes', 'price', 'image_url',
                  'image',)

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        sub_friendly_names = [(s.id,
                              s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names
        self.fields['subcategory'].choices = sub_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0 input-shadow'
