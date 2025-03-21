#!/usr/bin/python3

import subprocess
import re
import requests
import json

# Run this command to generate an access token
# Add the client id and client secret
command = ["curl -v https://dmptool.org/oauth/token -X POST -H \"Accept: application/json\" -d \"grant_type=client_credentials&client_id=[YOUR_CLIENT_ID]&client_secret=[YOUR_CLIENT_SECRET]\""]

process = subprocess.run(command, capture_output=True, text=True, shell=True)

access_token = ''

# Extract the access token
if process.returncode == 0:
    print("Command executed successfully:")
    match = re.search(r'"access_token"\s*:\s*"([^"]+)"', process.stdout)

    if match:
        access_token = match.group(1)
        print("Access Token: ", access_token)
else:
    print("Command failed with error:")
    print(process.stderr)

# API URL
base_url = 'https://dmptool.org/api/v2'

# Specify the endpoint you want to access, e.g., 'plans', 'templates'
endpoint = '/plans'

# Leave blank to query all plans
# To search for individual plans, use '/12345' (e.g., '/126595')
one_plan = '/126595'

api_url = f'{base_url}{endpoint}{one_plan}'

# access_token generated with call above
headers = {'Authorization': 'Bearer ' + access_token}

# Run the API query
try:
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    # Assuming the response is in JSON format
    data = response.json()
    print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except json.JSONDecodeError:
    print("Failed to decode JSON response")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

###
##
# When querying one plan at a time, you can extract data as so...
##
###


# Parse JSON as follows:

# title
print (data['items'][0]['dmp']['title'])

# Description
#print (data['items'][0]['dmp']['description'])

# DMP ID
#print (data['items'][0]['dmp']['dmp_id']['identifier'])

# Contributors (just the first one)
#print (data['items'][0]['dmp']['contributor'][0]['name'])

# Project information. Title and description are also here
#print (data['items'][0]['dmp']['project'][0])

# Project details like funder
#print (data['items'][0]['dmp']['project'][0]['funding'][0]['name'])

# Project funding opportunity URL
#print (data['items'][0]['dmp']['project'][0]['funding'][0]['grant_id']['identifier'])

# Project details like funding status
#print (data['items'][0]['dmp']['project'][0]['funding'][0]['funding_status'])

# What DMP template was used?
#print (data['items'][0]['dmp']['dmproadmap_template']['title'])

# Project expected dataset
#print (data['items'][0]['dmp']['dataset'][0]['type'])
#print (data['items'][0]['dmp']['dataset'][0]['title'])
#print (data['items'][0]['dmp']['dataset'][0]['description'])
#print (data['items'][0]['dmp']['dataset'][0]['keyword'])
