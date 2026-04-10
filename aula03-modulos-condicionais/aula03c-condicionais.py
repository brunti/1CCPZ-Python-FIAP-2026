idade = 20
maior_idade = idade >= 18
print(maior_idade, type(maior_idade))

#OPERADORES LOGICOS
# OR, AND, NOT
#LOGICA BOOLEANA

verifica_email = True
verifica_senha = False

print()#PULA UMA LINHA

login = verifica_email and verifica_senha
print(login)
if not login:
    print("Ow... seja mais inteligente!")



print()


#NOTAS.........


nota_final = 6
if nota_final < 4:
    print("Reprovado")

elif nota_final < 6:
    print("Recuperação")

else:
    print("Aprovado")


print("FIM")