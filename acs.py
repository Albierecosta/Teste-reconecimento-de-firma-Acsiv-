from datetime import date
today = date.today()

# dd/mm/YY
dta = today.strftime("%d/%m/%Y")
dataat = str(input('Data emissao: (caso for a data atual precione a tecla (x))'))
if dataat == 'x':
    dataat2 = dta
else:
    dataat2 = dataat    

#dta = str(input('Digite a data da emissao: '))
ins = 'isento'
insento = str(input('Qual valor do emolumento? (se for isento digite ins) '))

if insento == 'ins':
    insento2 = ins
else:
    insento2 = insento

s = 'Semelhança'
a = 'Autenticidade'
tipo = str(input('Digite (s) para semelhança, (a) para autenticidade: '))
if tipo == 's':
   tipo2 = s
else:
    tipo2 = a
qtp = int(input('Quantas pessoas são? '))
pessoas = list()

for i in range(qtp):
    nome = input('Nome: ')
    cpf = input('Cpf: ')
    pessoas.append([nome, cpf])
    
quantidade = int(input('Quantidade de etiquetas? '))

#print(pessoas, tipo2, insento2, dta,)

for x in range(quantidade):
   
    print('________________Reconhecimento de Firma_________')
    print('|   Reconheço por {} a(s) firmas de:       '.format(tipo2))       
    print('|{}                                    '.format(pessoas))
    print('|                                        ')
    print('|Pará de Minas, {}                      '.format(dataat2))
    print('|Valor dos Emolumentos: {}               '.format(insento2))
    print('_________________________________________________')