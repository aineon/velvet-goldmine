from django import forms
from .models import BlogPost
from .widgets import CustomClearableFileInput


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'slug': 'Slug',
            'author': 'Author',
            'intro': 'Intro',
            'section_one': 'Section 1',
            'section_two': 'Section 2',
            'section_three': 'Section 3',
            'original_url': 'Article Link',
            'image': 'Image',
            'credit': 'Credit',
            'source': 'Source',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-shadow'
            self.fields[field].label = False
