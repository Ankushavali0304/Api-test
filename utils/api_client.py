import requests


class APIClient:
    def __init__(self, base_url, auth_token=None):
        self.base_url = base_url
        self.session = requests.Session()
        if auth_token:
            self.session.headers.update({
                "Authorization": f"Bearer {auth_token}",
                "Content-Type": "application/json"
            })

    def get(self, endpoint, params=None, headers=None):
        return self.session.get(f"{self.base_url}{endpoint}", params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        return self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        return self.session.put(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=headers)
