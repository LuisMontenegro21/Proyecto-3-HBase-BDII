from DDL import *
from functions import *

def menu():
    print("+++++++++++++++++++++++++++++++++++++")
    print("++++++Human Resources Interface++++++")
    print("+++++++++++++++++++++++++++++++++++++")
    try:
        while True:
            print("1. Create Table")
            print("2. List Tables")
            print("3. Disable Table")
            print("4. Is Enabled")
            print("5. Alter Table")
            print("6. Drop Table")
            print("7. Drop All Tables")
            print("8. Describe Table")
            print("9. Insert Record")
            print("10. Display Data")
            print("11. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                table_name = input("Enter table name: ")
                create_table(table_name)
            elif choice == '2':
                list_tables()
            elif choice == '3':
                table_name = input("Enter table name: ")
                disable_table(table_name)
            elif choice == '4':
                table_name = input("Enter table name: ")
                is_enabled(table_name)
            elif choice == '5':
                table_name = input("Enter table name: ")
                alter_table(table_name)
            elif choice == '6':
                table_name = input("Enter table name: ")
                drop_table(table_name)
            elif choice == '7':
                drop_all_tables()
            elif choice == '8':
                table_name = input("Enter table name: ")
                describe_table(table_name)
            elif choice == '9':
                table_name = input("Enter table name: ")
                insert_record(table_name)
            elif choice == '10':
                table_name = input("Enter table name: ")
                display_data(table_name)
            elif choice == '11':
                break
            else:
                print("Invalid choice. Please try again.")

        

    except Exception as e:
        print(f"Error : {e}")

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    menu()