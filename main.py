from validacpf import ValidaCpf

recebe_cpf = str(input("Digite seu CPF: "))
cpf = ValidaCpf(recebe_cpf)

if cpf.valida():
    print('CPF Valido.')
else:
    print('CPF Invalido.')