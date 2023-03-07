import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        url = self.base_url + 'Misc/Cultures'
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers = headers)
        return response.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        url = self.base_url + 'Misc/Random-Address'
        payload = {
            "number": number,
            "culture": culture
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=payload, headers = headers)
        return response.json()

misc = Misc()
# print(misc.get_cultures('2d794c6f46094ceb96bd719c1c26c984'))
print(misc.get_random_address(api_key='2d794c6f46094ceb96bd719c1c26c984', number=715))

