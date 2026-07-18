import requests
response = requests.get("https://itunes.apple.com/search?entity=song&term=adele+taylor+swift+eminem")
data=response.json()
print(response.status_code)
for result in data["results"]:
    print("track:", result["trackName"])
    print("artist:" ,result["artistName"])
    print("collection:",result["collectionName"])