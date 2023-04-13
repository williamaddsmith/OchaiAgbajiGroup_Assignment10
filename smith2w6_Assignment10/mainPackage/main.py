#Name: Will Smith, Jared Skinner, James Davis
#email: smith2w6@mail.uc.edu
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can work with API keys, connect to the server, parse results into a dictionary, and extract the results
#Citations: https://api.nal.usda.gov/fdc/v1/foods/list
#Anything else that's relevant: N/A
#main.py
#api_key=DTRhuZrWjDMJkWZUhPJuxX9PE9MgoELBbKiCgt3h

import json
import requests
from iterateADictionaryPackage.iterateADictionary import *

response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DTRhuZrWjDMJkWZUhPJuxX9PE9MgoELBbKiCgt3h')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
iterate_dictionary(parsed_json[0])
#print(parsed_json)

print(parsed_json [2]['description']) # Extracting data from the dictionary