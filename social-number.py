import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        url = self.base_url + 'SocialNumber'
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()
socialnumber = SocialNumber()
print(socialnumber.get_SocialNumber("2d794c6f46094ceb96bd719c1c26c984"))