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
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return self.session.get(url, params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return self.session.post(url, data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return self.session.put(url, data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return self.session.delete(url, headers=headers)