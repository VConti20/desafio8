fila=["Ana", "Bruno", "Carla", "Diego"]

print(fila)
print(f"{fila[0]} foi atendida!")
print(f"{fila[2]} desistiu e saiu da fila!")
fila.remove("Carla")
print(fila)
fila.append("Eva")
print(f"{fila[-1]} entrou na fila!")
print(fila)

print(f"O proximo a ser atendido é {fila[0]}")