quantidade = int(input('Digite a quantidade de lugares necessario:'))

if(quantidade >= 80):
    print('Você tera que utilizar o auditorio alpha')
elif(quantidade < 80 & quantidade >=1):
    print('Utilize o auditorio Beta')
else:
    print('numero invalido')
