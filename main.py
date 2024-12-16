from servicios.api import obtener_datos
from modelos.todos import Todo
from modelos.users import User
from negocio.procesamiento import procesar_todos

def main():
    print("Bienvenido al sistema de gestión de datos")
    print("1. Obtener todos (tareas)")
    print("2. Obtener usuarios")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        todos_data = obtener_datos("todos")
        todos = [Todo(**todo) for todo in todos_data]
        stats = procesar_todos(todos)
        print("Estadísticas de tareas:", stats)
    elif opcion == "2":
        users_data = obtener_datos("users")
        users = [User(**user) for user in users_data]
        for user in users:
            print(user)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
