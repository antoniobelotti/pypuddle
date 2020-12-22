import json

import requests


class DataPuddle:

    def __init__(self, api_base_address):
        self.base_url = api_base_address

        response = requests.get(f"{self.base_url}/sessionkey")
        if response.status_code == 200:
            self.key = json.loads(response.content.decode('utf-8')).get("key")
        else:
            raise RuntimeError("unable to obtain api key")

    def cd(self, path):
        url = self.__get_endpoint("cd", path=path)
        response = requests.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("cd error. Specified path is probably non existent")

    def pwd(self):
        url = self.__get_endpoint("pwd")
        response = requests.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("PWD error")
        return json_response.get("path")

    def __get_endpoint(self, action, **kwargs):
        endpoint = f"{self.base_url}/{action}?key={self.key}"
        for key, item in kwargs.items():
            endpoint += f"&{key}={item}"
        return endpoint
