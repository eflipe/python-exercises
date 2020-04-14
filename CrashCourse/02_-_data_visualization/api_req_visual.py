import requests

from plotly.graph_objs import bar
from plotly import offline

# LLamar a la API y guardar la info
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
req = requests.get(url, headers=headers)
print(f'Status code: {req.status_code}')

# guardamos la respuesta de la API
# json() convierte el formato JSON en un diccionario de Py
response_dict = req.json()

# Explora la info sobre los reositores
repo_dicts = response_dict['items']

repo_names, stars, labels = [], [], []

for repo in repo_dicts:
    # Para los labels
    owner = repo['owner']['login']
    description = repo['description']
    link = repo['html_url']
    label = f'{owner}<br />{description}<br /><a href={link}>{link}</a>'

    repo_names.append(f'<a href="{repo["html_url"]}">{repo["name"]}</a>')
    stars.append(repo['stargazers_count'])
    labels.append(label)


# Visualización
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 3,
            'color': 'rgb(25, 25, 25)',
                }
    },
    'opacity': 0.6,
}]

layout = {
    'title': 'Ranking Python Projects',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')
