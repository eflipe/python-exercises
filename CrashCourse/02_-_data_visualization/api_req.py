import requests

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

print(response_dict.keys())
print(f'Respositores en total: {response_dict["total_count"]}')

# Explora la info sobre los reositores
repo_dicts = response_dict['items']
print(f'Total de repositorios: {len(repo_dicts)}')

# Primer repo
# repo_dict = repo_dicts[0]
# # print(f'\nKeys: {len(repo_dict)}')
# # for key in repo_dict.keys():
# #     print(key)
# print(f'\nInfo sobre el primer repo: ')
# print(f'Name: {repo_dict["name"]}')
# print(f'Owner/login: {repo_dict["owner"]["login"]}')
# print(f'Stars: {repo_dict["stargazers_count"]}')
# print(f'Repository: {repo_dict["html_url"]}')
# print(f'Created: {repo_dict["created_at"]}')
# print(f'Updated: {repo_dict["updated_at"]}')
# print(f'Description: {repo_dict["description"]}')
print(f'\nInfo sobre todos los repos: ')
for repo in repo_dicts:
    print(f'\nName: {repo["name"]}')
    print(f'Owner/login: {repo["owner"]["login"]}')
    print(f'Language: {repo["language"]}')
    print(f'Stars: {repo["stargazers_count"]}')
    print(f'Repository: {repo["html_url"]}')
    print(f'Created: {repo["created_at"]}')
    print(f'Updated: {repo["updated_at"]}')
    print(f'Description: {repo["description"]}')
