import requests

BASE_URL = "https://automationintesting.online/api"


class BaseAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def get(self, path: str):
        return self.session.get(f"{BASE_URL}{path}")

    def post(self, path: str, json=None):
        return self.session.post(f"{BASE_URL}{path}", json=json)

    def put(self, path: str, json=None):
        return self.session.put(f"{BASE_URL}{path}", json=json)

    def delete(self, path: str):
        return self.session.delete(f"{BASE_URL}{path}")
