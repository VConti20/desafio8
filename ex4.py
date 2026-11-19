convidados=[]

for i in range(5):
    nomes=input("Digite o nome do convidado(a): ")
    convidados.append(nomes)
convidados.sort()
print(f"Total de convidados: {len(convidados)}")

for nome in convidados:
    print(nome)