import psycopg2
import psycopg2.extras

host = 'localhost'
dbname = 'etiquetas'
user = 'postgres'
passoword = 'p.0300581-db'
sslmode = 'require'

# conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, passoword, sslmode)



from time import sleep
from datetime import date
today = date.today()

cidade = str(input('informe sua cidade: \n'))

arrayEmol = 'Emolumentos: '
id = "1"
print("\n---------------------------------------------")
print("Digite (1) para buscar a data atual.")
print("Digite (2) para digitar uma data valida.")
print("----------------------------------------------\n")
data = int(input(""))
if data <= 0:
     print("Opção invalida.")
     data = int(input("informe uma opção valida: "))
elif data > 2:
    print("Opção invalida.")
    data = int(input("informe uma opção valida: "))
elif data == 1:
    print("Buscando data atual...")
    sleep(1)  

def opcao1():
    global dataAtual
    dataAtual = today.strftime("%d/%m/%Y")

def opcao2():
    global dataAtual
    dataAtual = str(input("Informe uma data valida: "))

opcoes = { 1:opcao1, 2:opcao2}
opcoes.get(data)()

print("\n-------------------------------------------------")
print("Digite (1) para isento")
print("Digite (2) pra informa o valor dos emolumentos")
print("---------------------------------------------------\n")

calcula = int(input(""))
if calcula <= 0:
    print("Opção invalida.")
    calcula = int(input("informe uma opção valida: "))
elif calcula > 2:
    print("Opção invalida.")
    calcula = int(input("informe uma opção valida: "))
def opcao1():
    global valor
    valor = "Isento"
def opcao2(): 
    global valor
    valor = str(input("Digite o valor dos emolumentos: "))
opcoes = { 1:opcao1, 2:opcao2}
opcoes.get(calcula)()

print("\n-------------------------------")
print("Digite (1) para Autenticidade ")
print("Digite (2) para Semelhança\n")
print("---------------------------------\n")
recebe = int(input(""))
if recebe <= 0:
    print("Tipo digitado invalido.")
    recebe = int(input("Digite um tipo valido: "))
elif recebe > 2:
    print("Tipo digitado invalido.")
    recebe = int(input("Digite um tipo valido: "))
def opcao1():
    global tipo
    tipo = "Autenticidade"
def opcao2():
    global tipo
    tipo = "Semelhança"
opcoes = { 1:opcao1, 2:opcao2}
opcoes.get(recebe)()

arraynome = []
arraycpf = []

i = 0
quantidade = int(input("Quantidade de Partes: "))

for i in range(quantidade):
    nome = input("Digite seu nome: ")
    cpf = input("digite seu cpf: ")

    arraynome.append(nome)
    arraycpf.append(cpf)
print(len(arraynome))


quantidadeEtiqueta = int(input('Quantidade de etiquetas? \n'))

if quantidadeEtiqueta <= 0:
    print("Quantidade invalida")
    quantidadeEtiqueta = int(input('Quantidade de etiquetas? \n'))
   
arquivo = open("Partes.txt", "w")
for x in range(quantidadeEtiqueta):
    arquivo.write('Reconhecimento de Firma\n')
    arquivo.write('Reconheço por {} a(s) firmas de:\n'.format(tipo))
    for x in range(len(arraynome)): 
        arquivo.write('NOME: {}\n'.format(arraynome[x]))
        arquivo.write('CPF: {}\n'.format(arraycpf[x]))
    arquivo.write('{}, {}\n'.format(cidade,dataAtual))
    arquivo.write('{} {}\n'.format(arrayEmol, valor))
    arquivo.write('Quantidade de etiquetas: {}\n'.format(quantidadeEtiqueta))
    arquivo.write('\n')
arquivo.close()


for x in range(quantidadeEtiqueta):
    print('Reconhecimento de Firma')
    print('Reconheço por {} a(s) firmas de:'.format(tipo))
    for x in range(len(arraynome)):
            print('NOME: {}'.format(arraynome[x]))
            print('CPF: {}'.format(arraycpf[x]))    
    print('{}, {}'.format(cidade,dataAtual))
    print('{} {}'.format(arrayEmol, valor))
    print('Quantidade de etiquetas: {}\n'.format(quantidadeEtiqueta))
    
import csv
report = quantidade
with open("salva.csv", 'a+', newline='') as salva:
    escrever = csv.writer(salva)
    for i in range(1):
        for x in range(len(arraynome)):
            escrever.writerow([arraynome[x], arraycpf[x], valor, cidade, dataAtual, quantidade])


conn = psycopg2.connect(dbname=dbname, user=user, password=passoword, host=host)
# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur = conn.cursor()

# cur.execute("CREATE TABLE dados(id SERIAL PRIMARY KEY, partes VARCHAR, cpf VARCHAR, cidade VARCHAR, emolumentos VARCHAR, data VARCHAR, quantidade VARCHAR);")

for x in range(len(arraynome)):
    cur.execute("INSERT INTO dados(partes, cpf, data, quantidade, cidade, emolumentos, tipo) VALUES(%s, %s, %s, %s, %s, %s, %s)", (arraynome[x], arraycpf[x], dataAtual, quantidadeEtiqueta, cidade, valor, tipo))

conn.commit()

# conn.close()

print("conectado")