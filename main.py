from DDL import *
from DML import count, delete, deleteall, get, put, scan, truncate
from functions import *

def menu():
    print("+++++++++++++++++++++++++++++++++++++")
    print("++++++Human Resources Interface++++++")
    print("+++++++++++++++++++++++++++++++++++++")
    try:
        while True:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("1. Crear Tabla")
            print("2. Listar Tablas")
            print("3. Deshabilitar Tablas")
            print("4. Habilitar Tablas")
            print("5. Alterar Tabla")
            print("6. Borrar Tabla")
            print("7. Borrar Todas las Tablas")
            print("8. Describir Tabla")
            print("9. Insertar Datos")
            print("10. Mostrar Datos")
            print("11. Buscar Datos")
            print("12. Buscar Todos los Datos (scan)")
            print("13. Borrar Columna")
            print("14. Borrar Todas las Columnas")
            print("15. Contar Registros")
            print("16. Truncar Tabla")
            print("17. Salir")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            choice = str(input("Escribe el número de la opción que deseas: "))
            if choice == '1' or choice == 'create':
                table_name = input("Escribe el nombre de la tabla: ")
                namespace = get_namespace(table_name)
                create_table(table_name, namespace)
            elif choice == '2' or choice == 'list':
                list_tables()
            elif choice == '3' or choice == 'disable':
                table_name = input("Escribe el nombre de la tabla: ")
                disable_table(table_name)
            elif choice == '4' or choice == 'enable': 
                table_name = input("Escribe el nombre de la tabla: ")
                is_enabled(table_name)
            elif choice == '5' or choice == 'alter':
                table_name = input("Escribe el nombre de la tabla: ")
                alter_table(table_name)
            elif choice == '6' or choice == 'drop': 
                table_name = input("Escribe el nombre de la tabla: ")
                drop_table(table_name)
            elif choice == '7' or choice == 'dropall': 
                drop_all_tables()
            elif choice == '8' or choice == 'describe':
                table_name = input("Escribe el nombre de la tabla: ")
                describe_table(table_name)
            elif choice == '9' or choice == 'insert': 
                table_name = input("Escribe el nombre de la tabla: ")
                insert_record(table_name)
            elif choice == '10' or choice == 'display':
                table_name = input("Escribe el nombre de la tabla: ")
                display_data(table_name)
            elif choice == '11' or choice == 'search':
                table_name = input("Escribe el nombre de la tabla: ")
                row_key = input("Escribe el valor de la fila: ")
                record = get(table_name, row_key)
                if record:
                    print(json.dumps(record, indent=2))
            elif choice == '12' or choice == 'searchall':
                table_name = input("Escribe el nombre de la tabla: ")
                records = scan(table_name)
                if records:
                    for row_key, data in records.items():
                        print(f"Fila {row_key}: {json.dumps(data, indent=2)}")
            elif choice == '13' or choice == 'deletecol':
                table_name = input("Escribe el nombre de la tabla: ")
                row_key = input("Escribe el valor de la fila: ")
                column_family = input("Escribe el nombre de la familia de columnas: ")
                column = input("Escribe la columna:")
                delete(table_name, row_key, column_family, column)
            elif choice == '14' or choice == 'deleteallcol':
                table_name = input("Escribe el nombre de la tabla: ")
                row_key = input("Escribe el valor de la fila: ")
                deleteall(table_name, row_key)
            elif choice == '15' or choice == 'count':
                table_name = input("Escribe el nombre de la tabla: ")
                count(table_name)
            elif choice == '16' or choice == 'truncate':
                table_name = input("Escribe el nombre de la tabla: ")
                truncate(table_name)
            elif choice == '17' or choice == 'exit':
                break
            else:
                print("Invalid option, try again")
        
    except Exception as e:
        print(f"Error : {e}")

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    menu()
