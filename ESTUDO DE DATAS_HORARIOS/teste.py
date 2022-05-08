import datetime
def datas():
    ano = 2022
    mes = int(input('DIGITE O MÊS(em número de um algarismo) >>>'))
    dia = int(input('DIGITE O DIA>>>'))
    data1 = datetime.datetime(ano, mes, dia)
    return data1
while True:
    data = datas()
    op = input('mais uma s ou n?').lower()
    if op == 'n':
        break
dicio = {
    'armdata': data
}
print(dicio)