import urllib.parse
import requests

url = "https://twitter.com/search?q=clinton"

new_splited_url = list(urllib.parse.urlsplit(url))
encoded_qs = urllib.parse.urlencode({'q': '#trump'})
new_splited_url[3] = encoded_qs
new_url = urllib.parse.urlunsplit(new_splited_url)
response = requests.get(new_url)
with open('test.html') as f:
    f.write(requests.get(new_url).text)
