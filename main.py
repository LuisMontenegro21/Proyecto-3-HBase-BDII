from DDL import *
from DML import count, delete, deleteall, get, put, scan, truncate
from functions import *

def menu():
    print("+++++++++++++++++++++++++++++++++++++")
    print("++++++Human Resources Interface++++++")
    print("+++++++++++++++++++++++++++++++++++++")
    try:
        while True:
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
            choice = input("Escribe el número de la opción que deseas:")
            if choice == '1':
                table_name = input("Escribe el nombre de la tabla: ")
                create_table(table_name)
            elif choice == '2':
                list_tables()
            elif choice == '3':
                table_name = input("Escribe el nombre de la tabla: ")
                disable_table(table_name)
            elif choice == '4':
                table_name = input("Escribe el nombre de la tabla: ")
                is_enabled(table_name)
            elif choice == '5':
                table_name = input("Escribe el nombre de la tabla: ")
                alter_table(table_name)
            elif choice == '6':
                table_name = input("Escribe el nombre de la tabla: ")
                drop_table(table_name)
            elif choice == '7':
                drop_all_tables()
            elif choice == '8':
                table_name = input("Escribe el nombre de la tabla: ")
                describe_table(table_name)
            elif choice == '9':
                table_name = input("Escribe el nombre de la tabla: ")
                insert_record(table_name)
            elif choice == '10':
                table_name = input("Escribe el nombre de la tabla: ")
                display_data(table_name)
            elif choice == '11':
                table_name = input("Escribe el nombre de la tabla: ")
                row_key = input("Escribe el valor de la fila: ")
                record = get(table_name, row_key)
                if record:
                    print(json.dumps(record, indent=2))
            elif choice == '12':
                table_name = input("Escribe el nombre de la tabla: ")
                records = scan(table_name)
                if records:
                    for row_key, data in records.items():
                        print(f"Fila {row_key}: {json.dumps(data, indent=2)}")
            elif choice == '13':
                table_name = input("Escribe el nombre de la tabla: ")
                row_key = input("Escribe el valor de la fila: ")
                column_family = input("Escribe el nombre de la familia de columnas: ")
                column = input("Escribe la columna:")
                delete(table_name, row_key, column_family, column)
            elif choice == '14':
                table_name = input("Escribe el nombre de la tabla: ")
                row_key = input("Escribe el valor de la fila: ")
                deleteall(table_name, row_key)
            elif choice == '15':
                table_name = input("Escribe el nombre de la tabla: ")
                count(table_name)
            elif choice == '16':
                table_name = input("Escribe el nombre de la tabla: ")
                truncate(table_name)
            elif choice == '17':
                break
            else:
                print("Opción invalida. prueba otra vez")
        
    except Exception as e:
        print(f"Error : {e}")

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    menu()
