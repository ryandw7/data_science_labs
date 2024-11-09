import json
import sys

with open('./lab_data/python_data.json', 'r', encoding="latin-1") as f:
    data = json.load(f)
    print(data["labs"][0]["sections"][0]["tasks"][0]["solution"])