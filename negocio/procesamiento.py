# negocio/procesamiento.py

def procesar_todos(datos):
    """
    Procesa una lista de datos (usuarios o tareas).
    :param datos: Lista de diccionarios con datos.
    :return: Lista procesada.
    """
    if not datos:
        return "No hay datos para procesar."

    # Ejemplo: Extraer solo nombres de usuarios o títulos de tareas
    procesados = [item.get('name') or item.get('title') for item in datos if 'name' in item or 'title' in item]
    return procesados


def filtrar_por_clave(datos, clave, valor):
    """
    Filtra los datos por una clave y un valor específico.
    :param datos: Lista de diccionarios.
    :param clave: La clave por la cual filtrar.
    :param valor: El valor esperado.
    :return: Lista filtrada.
    """
    return [item for item in datos if item.get(clave) == valor]


def contar_elementos(datos):
    """
    Cuenta la cantidad de elementos en los datos.
    :param datos: Lista de diccionarios.
    :return: Entero con la cantidad de elementos.
    """
    return len(datos)
