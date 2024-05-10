from clients.callmebot_service import CallMeBot
from clients.conversor_service import CoinConversorService


conversor_service = CoinConversorService()
conversion = float(conversor_service.converter('BTC', 'BRL'))

wpp_service = CallMeBot()
wpp_service.send_message( message=f'Cotação do Bitcoin: R$ {conversion:.2f}')
