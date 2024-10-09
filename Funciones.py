from Validaciones import *

pacientes = []

#1)
def cargar_pacientes(pacientes):
    """
    Carga la información de pacientes en una lista anidada.

    Args:
        pacientes (list): Lista donde se almacenarán los datos de los pacientes.

    Returns:
        list: Lista actualizada con la información de los pacientes ingresados.
    """
    cantidad = int(input("Ingresa la cantidad de pacientes: "))
    
    for i in range(cantidad):
        historia_clinica = int(input(f"Ingresa el número de historia clínica del paciente {i+1}: "))
        nombre = input(f"Ingresa el nombre del paciente {i+1}: ")
        edad = int(input(f"Ingresa la edad del paciente {i+1}: "))
        diagnostico = input(f"Ingresa el diagnóstico del paciente {i+1}: ")
        internacion = int(input(f"Ingresa la cantidad de días de internación del paciente {i+1}: "))

        pacientes.append([historia_clinica, nombre, edad, diagnostico, internacion])
    return pacientes
#2)
def mostrar_pacientes(pacientes):
    """
    Muestra todos los pacientes registrados en la lista.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        print("Historia Clínica | Nombre | Edad | Diagnóstico | Días Internación")
        for paciente in pacientes:
            historia_clinica, nombre, edad, diagnostico, dias_internacion = paciente
            print(f"{historia_clinica} | {nombre} | {edad} | {diagnostico} | {dias_internacion}")
#3)
def buscar_pacientes(pacientes):
    """
    Busca un paciente por su número de historia clínica y muestra sus datos.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        historial = int(input("Ingresa el número de historia clínica del paciente que deseas buscar: "))
        for paciente in pacientes:
            if historial == paciente[0]:
                historia_clinica, nombre, edad, diagnostico, dias_internacion = paciente
                print(f"Historia Clínica: {historia_clinica}, Nombre: {nombre}, Edad: {edad}, Diagnóstico: {diagnostico}, Días Internación: {dias_internacion}")
                return
        print(f"No se encontró un paciente con el número de historia clínica {historial}.")
    return paciente
#4)
def ordenar_pacientes(pacientes):
    """
    Ordena la lista de pacientes por número de historia clínica en orden ascendente.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    print("Pacientes ordenados por número de historia clínica.")
    for paciente in pacientes:
        print(paciente)
#5)
def mayor_dias(pacientes):
    """
    Determina y muestra el paciente con más días de internación.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        max_paciente = pacientes[0]
        for paciente in pacientes:
            if paciente[4] > max_paciente[4]:
                max_paciente = paciente
        historia_clinica, nombre, edad, diagnostico, dias_internacion = max_paciente
        print(f"Paciente con más días de internación: {nombre} (Historia Clínica: {historia_clinica}) - Edad: {edad}, Diagnóstico: {diagnostico}, Días: {dias_internacion}.")
#6)
def menor_dias(pacientes):
    """
    Determina y muestra el paciente con menos días de internación.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        min_paciente = pacientes[0]
        for paciente in pacientes:
            if paciente[4] < min_paciente[4]:
                min_paciente = paciente
        historia_clinica, nombre, edad, diagnostico, dias_internacion = min_paciente
        print(f"Paciente con menos días de internación: {nombre} (Historia Clínica: {historia_clinica}) - Edad: {edad}, Diagnóstico: {diagnostico}, Días: {dias_internacion}.")
#7)
def mayor_cinco(pacientes):
    """
    Cuenta y muestra la cantidad de pacientes con más de 5 días de internación.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    contador = 0; limite = 5
    for i in range(len(pacientes)):
        if pacientes[i][4] >= limite:
            contador += 1
    print(f"La cantidad de pacientes con más de 5 días de internación es: {contador}.")
#8)
def promedio(pacientes):
    """
    Calcula y muestra el promedio de días de internación de todos los pacientes.

    Args:
        pacientes (list): Lista de pacientes.
        
    Returns:
        None
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        suma = 0
        for i in range(len(pacientes)):
            suma += pacientes[i][4]
        promedio = suma / len(pacientes)
        print(f"El promedio de días de internación de todos los pacientes es: {promedio:.2f}.")
    