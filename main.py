import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/get_ip_info/{item_id}")
def get_ip_info(item_id):
    # item_id = "122.164.83.83"
    url = f"http://ip-api.com/json/{item_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to retrieve IP information: {e}"}
