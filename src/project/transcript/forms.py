from django import forms

CHOICE_OPTIONS = [
    ('tiny', 'Tiny'),
    ('base', 'Base'),
    ('small', 'Small'),
]

class CreateTranscriptForm(forms.Form):
    model = forms.ChoiceField(choices=CHOICE_OPTIONS)
    file = forms.FileField(required=True)
