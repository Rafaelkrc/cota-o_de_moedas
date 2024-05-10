import requests
from decouple import config


class CallMeBot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = config('CALLMEBOT_API_KEY')
        self.__wts_phone = config('CELLPHONE')

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__wts_phone}&text={message}&apikey={self.__api_key}'
        )
        return response.text