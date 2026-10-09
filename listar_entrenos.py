import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HEVY_API_KEY")

respuesta = requests.get(
    "https://api.hevyapp.com/v1/workouts",
    headers={"api-key": api_key},
    params={"page": 1, "pageSize": 5},
)

datos = respuesta.json()

for entreno in datos["workouts"]:
    print(entreno["title"], "-", entreno["start_time"])