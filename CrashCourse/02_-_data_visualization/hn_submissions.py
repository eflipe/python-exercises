from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
res = requests.get(url)
print(f'Status code: {res.status_code}')

submission_ids = res.json()
submission_dicts = []

for id in submission_ids[:30]:
    # Pedimos un request para cada ID
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    res = requests.get(url)
    print(f"id: {id}\tstatus: {res.status_code}")
    response_dict = res.json()
    # Construimos el dictonario
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
