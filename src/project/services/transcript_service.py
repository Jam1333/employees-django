import requests
import project.settings

class TranscriptService:
    def transcribe_file(self, file, model="small", response_format="json"):
        """Creates a transcript for selected audio file without diarization"""
        
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
    
    def transcribe_file_with_diarization(self, file, model="small"):
        """Creates a transcript for selected audio file without diarization"""
        
        params = {
            "task": "transcribe",
            "word_timestamps": False,
            "output_format": "json",
            "model": model,
            "diarize": True,
        }
        
        files = {
            "audio_file": file,
        }
        
        response = requests.post(f"{project.settings.WHISPERX_API_URL}/asr", params=params, files=files)
        json = response.json()
        
        print(json)
        
        return json
