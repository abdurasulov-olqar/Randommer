import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        url = self.base_url + 'Name'
        payload = {
            "nameType": nameType,
            "quantity": quantity
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params = payload, headers = headers)
        return response.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        url = self.base_url + 'Name/Suggestions'
        payloads = {
            "startingWords": startingWords
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params = payloads, headers = headers)
        return response.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        url = self.base_url + 'Name/Cultures'
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

name = Name()
# print(name.get_name(nameType='firstname', quantity = 12, api_key='2d794c6f46094ceb96bd719c1c26c984'))
print(name.get_name_suggestions("2d794c6f46094ceb96bd719c1c26c984","ali"))