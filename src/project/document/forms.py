from django import forms
from .models import Document
from django.core.validators import FileExtensionValidator

class DocumentForm(forms.ModelForm):
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['docx'])],
        required=True
    )

    class Meta:
        model = Document
        fields = ["title", "employees"]
