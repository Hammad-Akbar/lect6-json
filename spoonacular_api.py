import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

dotenv_path = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_path)

spoonacular_key = os.environ['SPOONACULAR_KEY']
url = "https://api.spoonacular.com/recipes/search?apiKey={}".format(spoonacular_key)

response = requests.get(url)
json_body = response.json()

'''
json_body is a dictionary
json_body["results"] gives an array
json_body["results"][0] gives the first element in an array
json.dumps(json_body["results"][0], indent=2) makes for easy readibility
'''

print(json.dumps(json_body["results"][0], indent=2))
