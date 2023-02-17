import requests
url = "https://archive.org/metadata/TheAdventuresOfTomSawyer_201303"

response = requests.get(url)
if response.status_code == 200:
    result = response.json()
    print("Name: {}".format(result["metadata"]["title"]))
    print("Subject: {}".format(result["metadata"]["subject"]))
else:

    print("Error: {}".format(response.status_code))
