import requests
import json

q = requests.get('http://localhost:5000/students/2')
r = q.json()
print(r['name'])