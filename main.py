from servicios.api import obtener_datos
from modelos.todos import Todo
from modelos.users import User
from negocio.procesamiento import procesar_todos
from datos.conexion import crear_tablas, insertar_users, insertar_todos, obtener_users, obtener_todos, insertar_user_manual, actualizar_user, eliminar_user

def main():
    crear_tablas()  #Asegurarse de que las tablas existan!!!1

    while True:
        print("\nBienvenido al sistema de gestión de datos")
        print("1. Obtener y guardar usuarios de la API")
        print("2. Obtener y guardar tareas de la API")
        print("3. Consultar usuarios almacenados")
        print("4. Consultar tareas almacenadas")
        print("5. Agregar un nuevo usuario (POST)")
        print("6. Actualizar un usuario existente (PUT)")
        print("7. Eliminar un usuario (DELETE)")
        print("8. Verificar contraseña de un Usuario.")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nObteniendo usuarios desde la API...")
            users_data = obtener_datos("users")
            users = [User(**user) for user in users_data]
            insertar_users(users)
            print(f"{len(users)} usuarios guardados en la base de datos.")

        elif opcion == "2":
            print("\nObteniendo tareas desde la API...")
            todos_data = obtener_datos("todos")
            for todo in todos_data: #se convierte el 'userId' a 'user_id' en los datos obtenidos
                todo["user_id"] = todo.pop("userId")
            todos = [Todo(**todo) for todo in todos_data] #se cream instancias de Todo con los datos corregidos

            insertar_todos(todos)
            print(f"{len(todos)} tareas guardadas en la base de datos.")


        elif opcion == "3":
            print("\nConsultando usuarios almacenados...")
            users = obtener_users()
            for user in users:
                print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

        elif opcion == "4":
            print("\nConsultando tareas almacenadas...")
            todos = obtener_todos()
            for todo in todos:
                print(f"ID: {todo['id']}, User ID: {todo['user_id']}, Title: {todo['title']}, Completed: {todo['completed']}")

        elif opcion == "5":
            print("\nAgregar un nuevo usuario:")
            id = input("ID: ")
            name = input("Nombre: ")
            username = input("Username: ")
            email = input("Email: ")
            phone = input("Teléfono: ")
            website = input("Sitio Web: ")
            address = input("Dirección: ")
            company = input("Compañía: ")
            password = input("Contraseña: ")

            user = User(id, name, username, email, password, address, phone, website, company)
            insertar_user_manual(user)


        elif opcion == "6":
            print("\nActualizar un usuario existente:")
            user_id = input("Ingrese el ID del usuario a actualizar: ")
            field = input("Campo a actualizar (name, username, email, phone, website, address, company): ")
            new_value = input(f"Nuevo valor para {field}: ")
            actualizar_user(user_id, field, new_value)

        elif opcion == "7":
            print("\nEliminar un usuario:")
            user_id = input("Ingrese el ID del usuario a eliminar: ")
            eliminar_user(user_id)

        elif opcion == "8":
            print("\nVerificar contraseña:")
            user_id = input("Ingrese el ID del usuario: ")
            input_password = input("Ingrese la contraseña a verificar: ")

            #se obtiene el user de bd
            users = obtener_users()
            user_data = next((u for u in users if u['id'] == int(user_id)), None)

            if user_data:
                user = User(
                    user_data['id'], user_data['name'], user_data['username'], 
                    user_data['email'], user_data['password'], user_data['address'],
                    user_data['phone'], user_data['website'], user_data['company']
                )

                #se verifica la contraseña
                if user.verify_password(input_password):
                    print("¡Contraseña correcta!")
                else:
                    print("Contraseña incorrecta.")
            else:
                print("Usuario no encontrado.")

        elif opcion == "9":
                    print("\nSaliendo del sistema. ¡Nos vemos:)!")
                    break

        else:
                    print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
