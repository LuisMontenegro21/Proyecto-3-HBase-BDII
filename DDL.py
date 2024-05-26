from schemas import schemas, tables, table_status
import os, json

'''Implement DDL functions for HBase proper simulation'''

def create_table():
    table_name = input("Enter table name: ")
    if table_name in schemas:
        tables[table_name] = {'schema': schemas[table_name], 'records': []}
        print(f"Table '{table_name}' created successfully.")
    else:
        print("Invalid table name. Valid names are: employees, departments, projects, candidates.")

def list_tables():
    print("Tables:")
    for table_name in tables.keys():
        print(f"- {table_name} ({table_status[table_name]})")

def create_table():
    table_name = input("Enter table name: ")
    if table_name in schemas:
        if table_name not in tables:
            tables[table_name] = {'schema': schemas[table_name], 'records': []}
            table_status[table_name] = 'enabled'
            print(f"Table '{table_name}' created and enabled.")
        else:
            print(f"Table '{table_name}' already exists.")
    else:
        print("Invalid table name. Valid names are: employees, departments, projects, candidates.")

def disable_table():
    table_name = input("Enter table name: ")
    if table_name in tables:
        table_status[table_name] = 'disabled'
        print(f"Table '{table_name}' is now disabled.")
    else:
        print("Table does not exist.")

def is_enabled():
    table_name = input("Enter table name: ")
    if table_name in tables:
        status = table_status.get(table_name, 'disabled')
        print(f"Table '{table_name}' is {'enabled' if status == 'enabled' else 'disabled'}.")
    else:
        print("Table does not exist.")

def drop_table():
    table_name = input("Enter table name: ")
    if table_name in tables:
        del tables[table_name]
        del table_status[table_name]
        if os.path.exists(f"{table_name}.avro"):
            os.remove(f"{table_name}.avro")
        print(f"Table '{table_name}' dropped.")
    else:
        print("Table does not exist.")

def drop_all_tables():
    tables.clear()
    table_status.clear()
    for table_name in schemas.keys():
        if os.path.exists(f"{table_name}.avro"):
            os.remove(f"{table_name}.avro")
    print("All tables dropped.")

def describe_table():
    table_name = input("Enter table name: ")
    if table_name in tables:
        print(json.dumps(tables[table_name]['schema'], indent=2))
    else:
        print("Table does not exist.")

def alter_table():
    table_name = input("Enter table name: ")
    if table_name in tables:
        print("1. Add Field")
        print("2. Remove Field")
        choice = input("Enter choice: ")
        if choice == '1':
            field_name = input("Enter new field name: ")
            field_type = input("Enter new field type (int, string, float): ")
            if field_type in ['int', 'string', 'float']:
                new_field = {"name": field_name, "type": field_type}
                tables[table_name]['schema']['fields'].append(new_field)
                print(f"Field '{field_name}' added to '{table_name}'.")
            else:
                print("Invalid field type.")
        elif choice == '2':
            field_name = input("Enter field name to remove: ")
            fields = tables[table_name]['schema']['fields']
            tables[table_name]['schema']['fields'] = [field for field in fields if field['name'] != field_name]
            print(f"Field '{field_name}' removed from '{table_name}'.")
        else:
            print("Invalid choice.")
    else:
        print(f"Table: {table_name} does not exist.")

