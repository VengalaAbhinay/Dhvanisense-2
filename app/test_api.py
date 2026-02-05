import base64
import requests

# Point this to one of your Tamil or Hindi mp3 files
FILE_TO_TEST = "data/ai/tamil/Record_2026-02-02-20-45-18_680d03679600f7af0b4c700c6b270fe7.mp3" 

def run_test():
    with open(FILE_TO_TEST, "rb") as f:
        encoded_audio = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "language": "tamil",
        "audioFormat": "mp3",
        "audioBase64": encoded_audio
    }
    
    headers = {"x-api-key": "ds_live_8f2a1c9e7b4d3f0a1c9e8f2a1c9e7b4d"}
    
    print(f"🚀 Sending {FILE_TO_TEST} to API...")
    # Add a timeout of 60 seconds to allow the Transformer to process on CPU
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/detect", 
        json=payload, 
        headers=headers,
        timeout=60 
    )
    
    print("\n--- API RESPONSE ---")
    print(response.json())

if __name__ == "__main__":
    run_test()