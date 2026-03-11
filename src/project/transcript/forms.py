from django import forms
from django.core.validators import FileExtensionValidator

CHOICE_OPTIONS = [
    ('tiny', 'Tiny'),
    ('base', 'Base'),
    ('small', 'Small'),
    ('large-v3', 'Large*'),
]

class CreateTranscriptForm(forms.Form):
    model = forms.ChoiceField(choices=CHOICE_OPTIONS)
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['docx'])],
        required=True
    )
