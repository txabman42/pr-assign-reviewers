import os
import sys
import json
import requests

if (os.environ['GITHUB_REPOSITORY'] is None):
    sys.exit('The env variable GITHUB_REPOSITORY is required')

if (os.environ['GITHUB_EVENT_PATH'] is None):
    sys.exit('The env variable GITHUB_EVENT_PATH is required')

URI = 'https://api.github.com'
API_HEADER = 'Accept: application/vnd.github.v3+json'
AUTH_HEADER = 'Authorization: token' + os.environ['GITHUB_TOKEN']

event_path = json.loads(os.environ['GITHUB_EVENT_PATH'])
print(event_path)
number = event_path[".pull_request.number"]
print('Number: ' + number)

print('GitHub event')
print(os.environ['GITHUB_EVENT_PATH'])

def get_pr_info():
    api_url = URI + '/repos/' + os.environ['GITHUB_REPOSITORY'] + '/pulls/' + number
    headers = {API_HEADER, AUTH_HEADER}
    response = requests.get(api_url, headers=headers)
    print(response)