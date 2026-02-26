import docx
import io

class FileService:
    def read_docx(self, file):
        file_content = io.BytesIO(file.read())
            
        # Open the document using python-docx
        document = docx.Document(file_content)
            
        # Extract text from paragraphs
        full_text = []
        for para in document.paragraphs:
            full_text.append(para.text)
            
        # Join the list of strings into a single string
        text_content = '\n'.join(full_text)
        
        return text_content