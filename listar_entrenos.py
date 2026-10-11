import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("HEVY_API_KEY")

respuesta = requests.get(
    "https://api.hevyapp.com/v1/workouts",
    headers={"api-key": api_key},
    params={"page": 1, "pageSize": 5},
)

datos = respuesta.json()

primero = datos["workouts"][0]

print()
print(primero["title"])

for ejercicio in primero["exercises"]:
    print(ejercicio["title"])
    for serie in ejercicio["sets"]:
        print(f"   {serie['weight_kg']} kg x {serie['reps']} reps")