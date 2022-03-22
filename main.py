#programa para calcular o Indice de massa corporal em python usando estrutura em sequencia
nome = input('digite o seu nome ')
alturaEmCm =(float) (input ('agora qual sua altura em metros ?'))
peso = (float) (input('agora digite o seu peso em quilos'))
imc =  (float)(peso/(alturaEmCm * alturaEmCm))

print(nome, ' o seu imc é de ', imc )
