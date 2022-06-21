import requests
from datetime import datetime

# El token aca abajo va seguido de el textobot, es decir sin paréntesis
base_url = "https://api.telegram.org/bot(token)/sendMessage"

#id de canal de Telegram: -10012******

parameters = {'chat_id' : '-10012*******', 'text' : 'CUALQUIER TEXTO O URL'}

resp = requests.get(base_url, data= parameters)
print(resp.text)
