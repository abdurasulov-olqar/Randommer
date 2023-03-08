import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url = self.base_url + 'Phone/Generate'
        payload = {
            "CountryCode": CountryCode,
            "Quantity": Quantity
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params = payload, headers=headers)
        return response.json()
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url = self.base_url + 'Phone/IMEI'
        payload = {
            "Quantity": Quantity
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params = payload, headers=headers)
        return response.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        url = self.base_url + 'Phone/Validate'
        payload ={
            "telephone": telephone,
            "CountryCode": CountryCode
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=payload, headers=headers)
        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        url = self.base_url + 'Phone/Countries'
        headres = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headres)
        return response.json()
    
phone = Phone()
print(phone.get_countries("2d794c6f46094ceb96bd719c1c26c984"))

