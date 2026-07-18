import requests
artistname = input("Enter Artist Name")
response = requests.get(f"https://itunes.apple.com/search?entity=song&term={artistname}")
data=response.json()
print(response.status_code)
print(data["resultCount"])

