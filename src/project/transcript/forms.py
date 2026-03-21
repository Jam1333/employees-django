from django import forms
from django.core.validators import FileExtensionValidator

MODEL_CHOICE_OPTIONS = [
    ('small', 'Small'),
    ('large-v3', 'Large*'),
]

DIARIZATION_CHOICE_OPTIONS = [
    (False, "No"),
    (True, "Yes"),
]

class CreateTranscriptForm(forms.Form):
    model = forms.ChoiceField(choices=MODEL_CHOICE_OPTIONS)
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])],
        required=True
    )
    use_diarization = forms.ChoiceField(choices=DIARIZATION_CHOICE_OPTIONS)
