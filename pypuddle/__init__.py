import json

import requests


class DataPuddle:

    def __init__(self, api_base_address):
        self.base_url = api_base_address

        response = requests.get(f"{self.base_url}/sessionkey")
        if response.status_code == 200:
            self.key = json.loads(response.content.decode('utf-8')).get("key")
        else:
            raise RuntimeError("Unable to obtain api key")

    def cd(self, path):
        url = self.__get_endpoint("cd", path=path)
        response = requests.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("CD error")

    def pwd(self):
        url = self.__get_endpoint("pwd")
        response = requests.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("PWD error")
        return json_response.get("path")

    def mkdir(self, dir_path):
        url = self.__get_endpoint("mkdir", path=dir_path)
        response = requests.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("MKDIR error")

    def store(self, file, filename):
        url = self.__get_endpoint("store", filename=filename)
        response = requests.post(url, file)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("STORE error")

    def retrieve(self, filename):
        url = self.__get_endpoint("retrieve", filename=filename)
        response = requests.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("RETRIEVE error")
        return json.loads(json_response.get("file"))

    def rm(self, filename):
        url = self.__get_endpoint("rm", filename=filename)
        response = requests.get(url)
        print(response.content.decode('utf-8'))
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response.get("outcome") == "error":
            raise RuntimeError("RM error")

    def __get_endpoint(self, action, **kwargs):
        endpoint = f"{self.base_url}/{action}?key={self.key}"
        for key, item in kwargs.items():
            endpoint += f"&{key}={item}"
        return endpoint
