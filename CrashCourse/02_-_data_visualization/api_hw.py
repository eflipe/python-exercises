import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
res = requests.get(url)
print(f'Status code: {res.status_code}')

response_dict = res.json()
readable_file = 'data/readable_file_hw_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
