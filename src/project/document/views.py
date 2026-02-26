from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm
from services.ollama_service import OllamaService
from services.file_service import FileService

def documents(request):
    documents = Document.objects.prefetch_related("employees").all()
    
    return render(request, "documents.html", {"documents": documents})

def create_document(request):
    if request.method == "POST":
        print(request.FILES)
        
        form = DocumentForm(request.POST, request.FILES)
        
        if form.is_valid():
            file_service = FileService()
            ollama_service = OllamaService()
            
            file = form.cleaned_data["file"]
            file_content = file_service.read_docx(file)
            
            summary = ollama_service.get_response(f"""
                Пожалуйста, предоставьте краткое изложение документа в 4-5 предложениях.
                Содержание документа: '{file_content}'
                **Верните только краткое изложение, ничего больше**
                """)
            
            document = form.save(commit=False)
            document.summary = summary
            
            document.save()
            form.save_m2m()
            
            return redirect("documents")
    else:
        form = DocumentForm()
    
    return render(request, "create-document-form.html", {"form": form})

def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    
    if request.method == "POST":
        document.delete()
    
    return redirect("documents")
