from calendar import day_abbr, month, month_abbr
import json
from numpy import number
import pyodbc
import requests
from datetime import datetime
from time import sleep

page = 1 

   # Dia de analise
dia = '19'
mes = '09'
ano = '2022'
page = str(page)
device_sn = 'DQH6BL20BP'	

url = ('http://server.growatt.com/v1/device/tlx/tlx_data?tlx_sn='+device_sn+'&start_date='+ano+'-'+mes+'-'+dia+'&end_date='+ano+'-'+mes+'-'+dia+'&\page='+page+'')
print(url)
header = {'Accept': 'application/json',
        'token': 'd9bdc30b71e97c6a38320b39450bcf2b'}

resposta = requests.post(url, headers=header)
objeto=  json.loads(resposta.text)
print(objeto)

tamanho = objeto['data']['count']