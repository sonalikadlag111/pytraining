import requests

class MyApi:
    def __init__(self, identifier):
        self.identifier = identifier
        self.metadata_url = f"https://archive.org/metadata/{self.identifier}"

    def get_metadata(self):
        response = requests.get(self.metadata_url)
        if response.status_code == 200:
            metadata = response.json()
            original_name = metadata.get("metadata", {}).get("title")
            subject = metadata.get("metadata", {}).get("subject")
            print(f"Original name: {original_name}")
            print(f"Subject: {subject}")
        else:
            print(f"Error retrieving metadata: {response.status_code}")

book = MyApi("TheAdventuresOfTomSawyer_201303")
book.get_metadata()