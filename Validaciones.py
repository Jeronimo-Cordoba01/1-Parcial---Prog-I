intentos = 3

def validar_historia_clinica():
    """
    Solicita el número de historia clínica del paciente.
    
    Returns:
        int: El número de historia clínica si es válido (mayor que 0),
        None: Si se exceden los intentos permitidos.
    """
    for i in range(intentos):
        historial_clinico = int(input(f"Ingresa el número de historia clínica del paciente {i + 1}: "))
        if historial_clinico > 0:
            return historial_clinico
        else:
            print(f"El valor debe ser mayor a 0. Reintente. {intentos - i - 1} intentos restantes.")
    print("Has excedido el número de intentos. Regresando al menú.")
    return None

def validar_nombre():
    """
    Solicita el nombre del paciente.
    
    Returns:
        str: El nombre del paciente si es válido (no vacío),
        None: Si se exceden los intentos permitidos.
    """
    for i in range(intentos):
        valor = input(f"Ingresa el nombre del paciente {i + 1}: ").strip()
        if valor != "":
            return valor
        else:
            print(f"El nombre no puede estar vacío. Reintente. {intentos - i - 1} intentos restantes.")
    print("Has excedido el número de intentos. Regresando al menú.")
    return None

def validar_edad():
    """
    Solicita la edad del paciente.
    
    Returns:
        int: La edad del paciente si es válida (número no negativo),
        None: Si se exceden los intentos permitidos.
    """
    for i in range(intentos):
        edad = int(input(f"Ingresa la edad del paciente {i + 1}: "))
        if edad >= 0:
            return edad
        else:
            print(f"La edad debe ser un número no negativo. Reintente. {intentos - i - 1} intentos restantes.")
    print("Has excedido el número de intentos. Regresando al menú.")
    return None

def validar_diagnostico():
    """
    Solicita el diagnóstico del paciente.
    
    Returns:
        str: El diagnóstico del paciente si es válido (no vacío),
        None: Si se exceden los intentos permitidos.
    """
    for i in range(intentos):
        valor = input(f"Ingresa el diagnóstico del paciente {i + 1}: ").strip()
        if valor != "":
            return valor
        else:
            print(f"El diagnóstico no puede estar vacío. Reintente. {intentos - i - 1} intentos restantes.")
    print("Has excedido el número de intentos. Regresando al menú.")
    return None

def validar_internacion():
    """
    Solicita la cantidad de días de internación del paciente.
    
    Returns:
        int: La cantidad de días de internación si es válida (número no negativo),
        None: Si se exceden los intentos permitidos.
    """
    for i in range(intentos):
        internacion = int(input(f"Ingresa la cantidad de días de internación del paciente {i + 1}: "))
        if internacion >= 0:
            return internacion
        else:
            print(f"La cantidad de días debe ser un número no negativo. Reintente. {intentos - i - 1} intentos restantes.")
    print("Has excedido el número de intentos. Regresando al menú.")
    return None

def validar_historial(pacientes):
    """
    Solicita el número de historia clínica para buscar un paciente.
    
    Args:
        pacientes (list): Una lista de pacientes donde cada paciente es una lista que incluye el número de historia clínica como 
        primer elemento.
    
    Returns:
        list: La información del paciente correspondiente si se encuentra,
        None: Si se exceden los intentos permitidos.
    """
    for i in range(intentos):
        historial = int(input(f"Ingresa el número de historia clínica del paciente que deseas buscar {i + 1}: "))
        for paciente in pacientes:
            if historial == paciente[0]:
                return paciente 
        print(f"No se encontró un paciente con el número de historia clínica {historial}. Reintente. {intentos - i - 1} intentos restantes.")
    print("Has excedido el número de intentos. Regresando al menú.")
    return None
