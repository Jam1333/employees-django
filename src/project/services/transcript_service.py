import requests
import project.settings

class TranscriptService:
    def transcribe_file(self, file, model="small", response_format="json"):
        data = {
            "model": model,
            "response_format": response_format,
        }
        
        files = {
            "file": file,
        }
        
        response = requests.post(f"{project.settings.WHISPERX_API_URL}/v1/audio/transcriptions", data=data, files=files)
        json = response.json()
        
        print(json)
        
        return json