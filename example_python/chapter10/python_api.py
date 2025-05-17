#!/usr/bin/python3

import requests

response = requests.get("https://api.github.com/users/alagbamoses-era/repos")
data = response.json()

#print('login: ', data["login"]) 
#print('Name: ', data.get('name'))
#print('public repo: ', data.get('public_repos'))
#print('followers:', data.get('followers'))
#print('following: ', data.get('following'))


print('\n\nRepositories')
for repo in data:
    print(f"{repo['name']} (stars: {repo['stargazers_count']})")


