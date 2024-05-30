from DDL import create_table, list_tables, disable_table, enable_table, alter_table, drop_table, describe_table, drop_all
from DML import count, delete, deleteall, get, put_record, scan, truncate
from functions import *

def menu():
    print("+++++++++++++++++++++++++++++++++++++")
    print("++++++Human Resources Interface++++++")
    print("+++++++++++++++++++++++++++++++++++++")
    try:
        while True:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("1. Crear Tabla 2. Listar Tablas 3. Deshabilitar Tablas")
            print("4. Habilitar Tablas 5. Alterar Tabla 6. Borrar Tabla")    
            print("7. Borrar Todas las Tablas 8. Describir Tabla 9. Insertar Datos (put)")
            print("10. Mostrar Datos 11. Buscar Datos 12. Buscar Todos los Datos (scan)")
            print("13. Borrar Columna 14. Borrar Todas las Columnas 15. Contar Registros")
            print("16. Truncar Tabla 17. Salir")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            choice = str(input("Escribe el número de la opción que deseas: "))
            if choice == '1' or choice == 'create': # create tables
                create_table()
            elif choice == '2' or choice == 'list': # list tables
                list_tables()
            elif choice == '3' or choice == 'disable': # disable tables
                disable_table()
            elif choice == '4' or choice == 'enable': # enable tables
                enable_table()
            elif choice == '5' or choice == 'alter': # alter tables
                alter_table()
            elif choice == '6' or choice == 'drop': # drop table
                drop_table()
            elif choice == '7' or choice == 'dropall':  # drop tables
                drop_all()
            elif choice == '8' or choice == 'describe': # describe table
                describe_table()
            elif choice == '9' or choice == 'put': # put on table
                put_record()
            elif choice == '10' or choice == 'display':
                table_name = input("Escribe el nombre de la tabla: ")
                display_data()
            elif choice == '11' or choice == 'get':
                get()
            elif choice == '12' or choice == 'scan':
                scan()
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
