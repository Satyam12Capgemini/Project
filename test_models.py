import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")

print("BASE_URL =", base_url)
print("API_KEY Found =", bool(api_key))

url = f"{base_url}/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json"
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=60
    )

    print("STATUS =", response.status_code)
    print("RESPONSE =")
    print(response.text)

except Exception as e:
    print("ERROR =", str(e))
