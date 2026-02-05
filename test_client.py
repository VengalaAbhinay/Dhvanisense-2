import base64
import requests
import os

API_URL = "http://127.0.0.1:8000/api/v1/detect"
HEADERS = {"x-api-key": "ds_live_8f2a1c9e7b4d3f0a1c9e8f2a1c9e7b4d"}

def test_file(file_path, lang="Tamil"):
    if not os.path.exists(file_path):
        print("❌ File not found:", file_path)
        return

    # 1. Read MP3 and encode to Base64
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
        encoded_string = base64.b64encode(audio_bytes).decode("utf-8")

    payload = {
        "language": lang,
        "audioFormat": "mp3",
        "audioBase64": encoded_string
    }

    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("✅ Response:")
            print(response.json())
        else:
            print("❌ Error Response:")
            print(response.text)

    except Exception as e:
        print("Request failed:", e)


if __name__ == "__main__":
    # ✅ Use raw string OR forward slashes
    test_file(r"data\human\hindi\AudioCutter_human female1.mp3", lang="Hindi")

    # You can test another file too:
    # test_file(r"data\human\tamil\sample1.mp3", lang="Tamil")
