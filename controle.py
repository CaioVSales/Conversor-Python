import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()

cotacao_dolar = float(cotacoes['USDBRL']['bid'])
#print('Cotação do dolar: '+ cotacao_dolar)
real_d = float(input('Digite o valor em Dólar para converter em Real: '))
valor_dolar = real_d * cotacao_dolar
print(valor_dolar)

cotacao_euro = float(cotacoes['EURBRL']['bid'])
#print('Cotação do euro: '+ cotacao_euro)
real_e = float(input('Digite o valor em Euro para converter em Real: '))
valor_euro = real_e * cotacao_euro
print(valor_euro)

cotacao_bitcoin = float(cotacoes['BTCBRL']['bid'])
#print('Cotação do bitcoin: '+ cotacao_bitcoin)
real_b = float(input('Digite o valor em Bitcoin para converter em Real: '))
valor_bitcoin = real_b * cotacao_bitcoin
print(valor_bitcoin)


#euro/dolar
euro_dolar = float(input('Digite o valor em Euro para converter em Dólar: '))
valor_ed = cotacao_euro / cotacao_dolar
valor_ced = valor_ed * euro_dolar
print(valor_ced)

#euro/bitcoin
bitcoin_euro = float(input('Digite o valor em Bitcoin para converter em Euro: '))
valor_be = cotacao_bitcoin / cotacao_euro
valor_cbe = valor_be * bitcoin_euro
print(valor_cbe)

#dolar/bitcoin
bitcoin_dolar = float(input('Digite o valor em Bitcoin para converter em Dólar: '))
valor_bd = cotacao_bitcoin / cotacao_dolar
valor_cbd = valor_bd * bitcoin_dolar
print(valor_cbd)