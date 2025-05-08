import requests


class APIClient:
    BASE_URLS = {}

    def __init__(self, service_name: str, auth_token: str = None):
        if service_name not in self.BASE_URLS:
            print(self.BASE_URLS)
            raise ValueError(f"Unknown service: {service_name}")

        self.base_url = self.BASE_URLS[service_name].rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

        if auth_token:
            self.session.headers["Authorization"] = f"Bearer {auth_token}"

    def get(self, endpoint, params=None, headers=None):
        return self.session.get(f"{self.base_url}{endpoint}", params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        return self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        return self.session.put(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=headers)
