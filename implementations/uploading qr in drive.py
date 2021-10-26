import json
import requests
headers = {"Authorization": "Bearer ya29.a0ARrdaM8H6XRE55EjI9HOH4sfvPAcqgyk2vC2NNDmUTs7W15lIoCAm3ZQkXtUbLtbUwNIkrwxr1-pEf3z4Jpd8VFPCFhzgT9zBkdlcU_kKudf4AEGyo40DTtcNtju-4FkpJU_iNy1LLq4U8wKfOyDYSMtnSAF"}
para = {
    "name": "mycode.png",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("mycode.png", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)


