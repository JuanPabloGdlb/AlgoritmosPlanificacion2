import time  # Importa el módulo 'time' para trabajar con el tiempo, en este caso los segundos.

# Función para cargar y analizar cada línea del archivo para separar los datos relevantes.
def cargar_procesos(nombre_archivo):
    procesos = []  # Inicializa una lista vacía llamada 'procesos' para almacenar los datos del archivo.
    with open(nombre_archivo, 'r') as archivo:  # Abre el archivo especificado en modo lectura ('r').
        for linea in archivo:  # Itera a través de cada línea del archivo.
            proceso, tiempo, prioridad = linea.strip().split(', ')  # Divide cada línea en sus componentes y los asigna a variables.
            procesos.append((proceso, int(tiempo), int(prioridad)))  # Agrega una tupla con los datos a la lista 'procesos'.
    return procesos  # Retorna la lista de procesos una vez que se han cargado y parseado los datos del archivo.

# Algoritmo de Round Robin
def round_robin(procesos):
    quantum = 3
    tiempo_total = 0  # Inicializa una variable 'tiempo_total' para rastrear el tiempo total de ejecución.
    while procesos:  # Mientras haya procesos en la lista 'procesos'.
        proceso, tiempo, prioridad = procesos.pop(0)  # Obtiene y remueve el primer proceso de la lista.
        tiempo_actual = min(tiempo, quantum)  # Calcula el tiempo actual de ejecución como el mínimo entre 'tiempo' y 'quantum'.
        print(f"Ejecutando {proceso} durante {tiempo_actual} segundos")  # Imprime información sobre la ejecución del proceso.
        tiempo -= tiempo_actual  # Reduce el tiempo restante del proceso.
        tiempo_total += tiempo_actual  # Actualiza el tiempo total de ejecución.
        if tiempo > 0:  # Si aún queda tiempo por ejecutar para este proceso, lo vuelve a agregar a la lista.
            procesos.append((proceso, tiempo, prioridad))
    print(f"Tiempo total de ejecución: {tiempo_total} segundos")  # Imprime el tiempo total de ejecución al final.

# Algoritmo SJF
def sjf(procesos): # sort se utiliza para ordenar los elementos de una lista en su lugar.
    procesos.sort(key=lambda x: x[1])  # Ordena la lista de procesos en función de sus tiempos de ejecución (orden Shortest Job First).
    tiempo_total = 0  # Inicializa una variable para rastrear el tiempo total de ejecución.
    for proceso, tiempo, prioridad in procesos:  # Itera a través de la lista de procesos ordenada.
        print(f"Ejecutando {proceso} durante {tiempo} segundos")  # Imprime información sobre la ejecución del proceso.
        tiempo_total += tiempo  # Actualiza el tiempo total de ejecución.
    print(f"Tiempo total de ejecución: {tiempo_total} segundos")  # Imprime el tiempo total de ejecución al final.

# Algoritmo FIFO
def fifo(procesos):
    tiempo_total = 0  # Inicializa una variable para rastrear el tiempo total de ejecución.
    for proceso, tiempo, prioridad in procesos:  # Itera a través de la lista de procesos en orden de llegada (First-In, First-Out).
        print(f"Ejecutando {proceso} durante {tiempo} segundos")  # Imprime información sobre la ejecución del proceso.
        tiempo_total += tiempo  # Actualiza el tiempo total de ejecución.
    print(f"Tiempo total de ejecución: {tiempo_total} segundos")  # Imprime el tiempo total de ejecución al final.

# Algoritmo de Prioridades
def prioridades(procesos): # sort se utiliza para ordenar los elementos de una lista en su lugar.
    procesos.sort(key=lambda x: x[2])  # Ordena la lista de procesos por prioridad.
    tiempo_total = 0  # Inicializa una variable para rastrear el tiempo total de ejecución.
    for proceso, tiempo, prioridad in procesos:  # Itera a través de la lista de procesos ordenada por prioridad.
        print(f"Ejecutando {proceso} durante {tiempo} segundos")  # Imprime información sobre la ejecución del proceso.
        tiempo_total += tiempo  # Actualiza el tiempo total de ejecución.
    print(f"Tiempo total de ejecución: {tiempo_total} segundos")  # Imprime el tiempo total de ejecución al final.

# Función para agregar un nuevo proceso al archivo
def agregar_proceso(nombre_archivo):
    #Se solicita al usuario que ingrese el nombre, el tiempo, la prioridad y la ubicacion del proceso.
    proceso = input("Ingrese el nombre del proceso: ")
    tiempo = input("Ingrese el tiempo de duración del proceso: ")
    prioridad = input("Ingrese la prioridad del proceso: ")
    #Debe estar en minusculas abajo/arriba.
    ubicacion = input("¿Desea agregarlo al principio o al final del archivo? (arriba/abajo): ").lower()

    # Verificar si la ubicación es "arriba" o "abajo"
    if ubicacion == "arriba":
        #Se abre el archivo en modo lectura ('r') y se lee su contenido completo. El contenido del archivo se almacena en la variable contenido.
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        #Se abre el archivo en modo escritura ('w'). Se crea una línea de texto nuevo_proceso
        #que contiene el nombre del proceso, el tiempo y la prioridad, separados por comas, seguido de un salto de línea ('\n').
        with open(nombre_archivo, 'w') as archivo:
            nuevo_proceso = f"{proceso}, {tiempo}, {prioridad}\n"
            archivo.write(nuevo_proceso + contenido)
    else:  # Agregar al final por defecto
        #Si la respuesta del usuario es "abajo", se ejecuta la rama else,
        #que significa que el proceso se agregará al final del archivo por defecto.
        #Se abre el archivo en modo adición ('a') y se escribe el nuevo proceso al final del archivo.
        with open(nombre_archivo, 'a') as archivo:
            nuevo_proceso = f"{proceso}, {tiempo}, {prioridad}\n"
            archivo.write(nuevo_proceso)

# Función para mostrar el menú
def menu():
    print("Selecciona el algoritmo de planificación:")
    print("1. Round Robin")
    print("2. SJF (el más corto primero)")
    print("3. FIFO (el primero en llegar, el primero en salir)")
    print("4. Prioridades")
    print("5. Salir")
    print("6. Agregar nuevo proceso")

while True:  
    menu()  
    opcion = input("Ingresa el número de la opción que deseas ejecutar: ")

    if opcion == '1':
        procesos = cargar_procesos("texto.txt")
        print("\nAlgoritmo Round Robin:")
        round_robin(procesos.copy())
    elif opcion == '2':
        procesos = cargar_procesos("texto.txt")
        print("\nAlgoritmo SJF:")
        sjf(procesos.copy())
    elif opcion == '3':
        procesos = cargar_procesos("texto.txt")
        print("\nAlgoritmo FIFO:")
        fifo(procesos.copy())
    elif opcion == '4':
        procesos = cargar_procesos("texto.txt")
        print("\nAlgoritmo de Prioridades:")
        prioridades(procesos.copy())
    elif opcion == '5':
        break
    elif opcion == '6': 
        agregar_proceso("texto.txt")
        print("Proceso agregado al archivo.")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
