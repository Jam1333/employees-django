from django.shortcuts import render, redirect
from .forms import DocumentForm
from services.ollama_service import OllamaService

def create_document(request):
    if request.method == "POST":
        print(request.FILES)
        
        form = DocumentForm(request.POST, request.FILES)
        
        if form.is_valid():
            service = OllamaService()
            
            file_content = form.cleaned_data["file"].read().decode("utf-8")
            summary = service.get_response(f"""
                Please provide 4-5 sentences summary of the document
                Document content: '{file_content}'
                **Return only summary, nothing else**
                """)
            
            document = form.save(commit=False)
            document.summary = summary
            
            document.save()
            
            return render(request, "create-document-form.html", {"form": form})
    else:
        form = DocumentForm()
    
    return render(request, "create-document-form.html", {"form": form})
