from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", SCOPES
)
credentials = flow.run_console()

youtube = build("youtube", "v3", credentials=credentials)

with open("metadata.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

title = lines[0].strip()
description = "".join(lines[2:])

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": "27"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("final_video.mp4")
)

response = request.execute()
print("Uploaded video ID:", response["id"])
