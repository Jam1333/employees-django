from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateTranscriptForm
from services.transcript_service import TranscriptService
import json

def create_transcript(request):
    if request.method == "POST":
        print(request.FILES)
        
        form = CreateTranscriptForm(request.POST, request.FILES)
        
        if form.is_valid():
            service = TranscriptService()
            
            transcript = service.transcribe_file(
                form.cleaned_data["file"],
                form.cleaned_data["model"],
                "verbose_json",
            )
            
            formatted_json_transcript = json.dumps(transcript, indent=4, ensure_ascii=False)
            
            response = HttpResponse(formatted_json_transcript, content_type="text/plain")
            response["Content-Disposition"] = 'attachment; filename="transcript.json"'
            
            return response
    else:
        form = CreateTranscriptForm()
    
    return render(request, "create-transcript-form.html", {"form": form})