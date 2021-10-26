from PyQt5 import uic, QtWidgets
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()

cotacao_dolar = float(cotacoes['USDBRL']['bid'])
cotacao_euro = float(cotacoes['EURBRL']['bid'])
cotacao_bitcoin = float(cotacoes['BTCBRL']['bid'])

def funcao_principal():

    if janela.Euro1.isChecked() and janela.Dolar2.isChecked():
        valor_ed = cotacao_euro / cotacao_dolar
        a = float(janela.Moeda1.text())
        valor_ced = a * valor_ed
        print(valor_ced)
        b = str(valor_ced)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Dolar1.isChecked() and janela.Euro2.isChecked():
        valor_ed = cotacao_dolar / cotacao_euro
        a = float(janela.Moeda1.text())
        valor_ced = a * valor_ed
        print(valor_ced)
        b = str(valor_ced)
        janela.Convertido.setText('Valor convertido: ' + b)
    
    elif janela.Euro1.isChecked() and janela.Real2.isChecked():
        valor_re = cotacao_euro
        a = float(janela.Moeda1.text())
        valor_cre = a * valor_re
        print(valor_cre)
        b = str(valor_cre)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Dolar1.isChecked() and janela.Real2.isChecked():
        valor_rd = cotacao_dolar
        a = float(janela.Moeda1.text())
        valor_crd = a * valor_rd
        print(valor_crd)
        b = str(valor_crd)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Bitcoin1.isChecked() and janela.Real2.isChecked():
        valor_rb = cotacao_bitcoin
        a = float(janela.Moeda1.text())
        valor_crb = a * valor_rb
        print(valor_crb)
        b = str(valor_crb)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Bitcoin1.isChecked() and janela.Dolar2.isChecked():
        valor_bd = cotacao_bitcoin / cotacao_dolar
        a = float(janela.Moeda1.text())
        valor_cbd = a * valor_bd
        print(valor_cbd)
        b = str(valor_cbd)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Bitcoin1.isChecked() and janela.Euro2.isChecked():
        valor_be = cotacao_bitcoin / cotacao_euro
        a = float(janela.Moeda1.text())
        valor_cbe = a * valor_be
        print(valor_cbe)
        b = str(valor_cbe)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Euro1.isChecked() and janela.Bitcoin2.isChecked():
        valor_eb = cotacao_euro / cotacao_bitcoin
        a = float(janela.Moeda1.text())
        valor_ceb = a * valor_eb
        print(valor_ceb)
        b = str(valor_ceb)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Dolar1.isChecked() and janela.Bitcoin2.isChecked():
        valor_db = cotacao_dolar / cotacao_bitcoin
        a = float(janela.Moeda1.text())
        valor_cdb = a * valor_db
        print(valor_cdb)
        b = str(valor_cdb)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Dolar1.isChecked() and janela.Dolar2.isChecked():
        valor_dd = cotacao_dolar / cotacao_dolar
        a = float(janela.Moeda1.text())
        valor_cdd = a * valor_dd
        b = str(valor_cdd)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Euro1.isChecked() and janela.Euro2.isChecked():
        valor_ee = cotacao_euro / cotacao_euro
        a = float(janela.Moeda1.text())
        valor_cee = a * valor_ee
        b = str(valor_cee)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Bitcoin1.isChecked() and janela.Bitcoin2.isChecked():
        valor_bb = cotacao_bitcoin / cotacao_bitcoin
        a = float(janela.Moeda1.text())
        valor_cbb = a * valor_bb
        b = str(valor_cbb)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Real1.isChecked() and janela.Dolar2.isChecked():
        a = float(janela.Moeda1.text())
        valor_rd = a / cotacao_dolar
        b = str(valor_rd)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Real1.isChecked() and janela.Euro2.isChecked():
        a = float(janela.Moeda1.text())
        valor_re = a / cotacao_euro
        b = str(valor_re)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Real1.isChecked() and janela.Bitcoin2.isChecked():
        a = float(janela.Moeda1.text())
        valor_rb = a / cotacao_bitcoin
        b = str(valor_rb)
        janela.Convertido.setText('Valor convertido: ' + b)

    elif janela.Real1.isChecked() and janela.Real2.isChecked():
        a = float(janela.Moeda1.text())
        valor_rr = a
        b = str(valor_rr)
        janela.Convertido.setText('Valor convertido: ' + b)




app = QtWidgets.QApplication([])
janela = uic.loadUi("janela.ui")
janela.Converter.clicked.connect(funcao_principal)

janela.show()
app.exec()