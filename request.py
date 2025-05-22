import requests

url = 'https://prts.wiki/api.php'
params = {
    'action': 'query',
    'format': 'json',
    'titles': '阿米娅',
    'prop': 'extracts',
    'exintro': True,
    'explaintext': True,
}

response = requests.get(url, params=params)
data = response.json()

page = next(iter(data['query']['pages'].values()))
print(page['extract'])