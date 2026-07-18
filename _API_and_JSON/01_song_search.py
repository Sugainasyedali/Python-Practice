import requests
response = requests.get("https://itunes.apple.com/search?entity=song&term=adele")
data=response.json()
print(response.status_code)
for result in data["results"]:
    print(result["trackName"])