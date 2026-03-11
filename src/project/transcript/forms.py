from django import forms

CHOICE_OPTIONS = [
    ('tiny', 'Tiny'),
    ('base', 'Base'),
    ('small', 'Small'),
    ('large-v3', 'Large*'),
]

class CreateTranscriptForm(forms.Form):
    model = forms.ChoiceField(choices=CHOICE_OPTIONS)
    file = forms.FileField(required=True)
