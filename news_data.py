import requests
url = ('https://newsapi.org/v2/everything?'
		'q=Apple&'
		'from=2013-04-01&'
       'apiKey=bf9eb8c9353d4bb7a68f44f6bbc13a72')
response = requests.get(url)
print response.json()