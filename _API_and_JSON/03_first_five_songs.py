import requests
response = requests.get("https://itunes.apple.com/search?entity=song&term=adele+taylor+swift+eminem")
data=response.json()
print(response.status_code)
count = 0
for result in data["results"]:
    if count < 5:
     print(result["trackName"])
     count +=1