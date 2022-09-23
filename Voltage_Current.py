from calendar import day_abbr, month, month_abbr
import json
from numpy import number
import pyodbc
import requests
from datetime import datetime
from time import sleep
import xlsxwriter

def requeste(page): 
    # Dia de analise
    dia = '22'
    mes = '09'
    ano = '2022'
    page = str(page)
    device_sn = ''	

    url = ('http://server.growatt.com/v1/device/tlx/tlx_data?tlx_sn='+device_sn+'&start_date='+ano+'-'+mes+'-'+dia+'&end_date='+ano+'-'+mes+'-'+dia+'&page='+page+'&perpage=100')

    header = {'Accept': 'application/json',
                'token': ''}

    resposta = requests.post(url, headers=header)
    objeto=  json.loads(resposta.text)
    print(url)

    return(objeto)

page = 1 
lista_dados = []

while page <= 1:

        print('page')
        print(page)
        objeto = requeste(page)

        contagem = 0
        tamanho = len(objeto['data']['datas'])
        print('VAI CMEÇAR O SHOW....tamanho')
        print(tamanho)
        sleep(3)

        while contagem < tamanho:

            print('---contagem---')
            print(contagem)
            print('---TAMANHO---')
            print(tamanho)

            print(objeto['data']['datas'][contagem]['time'])
            print(objeto['data']['datas'][contagem]['vpv1'])
            print(objeto['data']['datas'][contagem]['ipv1'])

            
            amostragem = {'horário':str(objeto['data']['datas'][contagem]['time']) , 'Voltagem_pv1':str(objeto['data']['datas'][contagem]['vpv1']),'Corrente_pv1':str(objeto['data']['datas'][contagem]['ipv1'])}
            lista_dados.append(amostragem)




            print('-------')
            print(page)
            contagem = contagem + 1


        contagem = 0
        page = page + 1
        print(page)
        print('Encerrou primeira pagina')


workbook = xlsxwriter.Workbook("AllAboutPythonExcel.xlsx")


worksheet = workbook.add_worksheet("TensãoxCorrente_tempo")
worksheet.write(0,0,"#")
worksheet.write(0,1,"Voltagem_pv1")
worksheet.write(0,2,"Corrente_pv1")
worksheet.write(0,3,"horário")


for index, entry in enumerate(lista_dados):
    worksheet.write(index+1,0, str(index))
    worksheet.write(index+1,1, entry["Voltagem_pv1"])
    worksheet.write(index+1,2, entry["Corrente_pv1"])
    worksheet.write(index+1,3, entry["horário"])

workbook.close()
        
print('----FIIIIIIM---')

