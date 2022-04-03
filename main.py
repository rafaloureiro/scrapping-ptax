destino = r"C:\Users\RAFA_\Downloads\Cotacoes.csv"
data_inicio = input('Inicio: ')
data_fim = input('Fim: ')

url = ("https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?"
    "method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI={}&DATAFIM={}").format(data_inicio, data_fim)

import requests

r = requests.get(url)
print(r)
print(r.content)

arquivo = open(destino, "wt")
arquivo.write(r.text)
arquivo.close()

