import json
import os

jsonData = 'books.json'

def readBookStore():
    if os.path.exists(jsonData):
        with open(jsonData,'r') as file:
            return json.load(file)

def writeToBookStore(data):
    with open(jsonData,'w') as file:
        json.dump(data, file, indent=4)