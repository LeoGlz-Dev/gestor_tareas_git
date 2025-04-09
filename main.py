print("Bienvenido a tu Gestor de Tareas :D")

with open("tareas.txt", "a") as archivo:
    tarea = input("Escribe una nueva tarea: ")
    archivo.write(tarea + "\n")
    print("Tarea guardada.")
