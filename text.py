import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        url = self.base_url + 'Text/LoremIpsum'
        payload = {
            "loremType": loremType,
            "type": type,
            "number": number
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=payload, headers=headers)
        return response.json()
    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        url = self.base_url + 'Text/Password'
        payload = {
            "length": length,
            "hasDigits": hasDigits,
            "hasUppercase": hasUppercase,
            "hasSpecial": hasSpecial
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=payload, headers=headers)
        return response.json()
text=Text()
print(text.generate_LoremIpsum(loremType="normal", type="words", number=101, api_key="2d794c6f46094ceb96bd719c1c26c984"))
