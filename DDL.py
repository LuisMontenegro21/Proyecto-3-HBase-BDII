from schemas import table_schemas, table_status
import os, json

'''Implement DDL functions for HBase proper simulation'''

def create_table(table_name):
    if table_name in table_schemas:
        os.makedirs(f"data/{table_name}", exist_ok=True)
        print(f"Table '{table_name}' created.")
    else:
        print("Invalid table name.")

def list_tables():
    tables = [d for d in os.listdir('data') if os.path.isdir(os.path.join('data', d))]
    print("Tables:")
    for table in tables:
        print(f"- {table} ({table_status[table]})")

def disable_table(table_name):
    if table_name in table_schemas:
        table_status[table_name] = 'disabled'
        print(f"Table '{table_name}' is now disabled.")
    else:
        print("Table does not exist.")

def is_enabled(table_name):
    if table_name in table_schemas:
        status = table_status[table_name]
        print(f"Table '{table_name}' is {'enabled' if status == 'enabled' else 'disabled'}.")
    else:
        print("Table does not exist.")

def alter_table(table_name):
    if table_name in table_schemas:
        print("1. Add Field")
        print("2. Remove Field")
        choice = input("Enter choice: ")
        if choice == '1':
            field_name = input("Enter new field name: ")
            field_type = input("Enter new field type (int, string, float): ")
            if field_type in ['int', 'string', 'float']:
                new_field = {"name": field_name, "type": field_type}
                table_schemas[table_name]['fields'].append(new_field)
                print(f"Field '{field_name}' added to '{table_name}'.")
            else:
                print("Invalid field type.")
        elif choice == '2':
            field_name = input("Enter field name to remove: ")
            fields = table_schemas[table_name]['fields']
            table_schemas[table_name]['fields'] = [field for field in fields if field['name'] != field_name]
            print(f"Field '{field_name}' removed from '{table_name}'.")
        else:
            print("Invalid choice.")
    else:
        print("Table does not exist.")

def drop_table(table_name):
    if table_name in table_schemas:
        region_dir = f"data/{table_name}"
        if os.path.exists(region_dir):
            for root, dirs, files in os.walk(region_dir, top_down=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(region_dir)
        print(f"Table '{table_name}' dropped.")
    else:
        print("Table does not exist.")

def drop_all_tables():
    for table_name in table_schemas.keys():
        drop_table(table_name)
    print("All tables dropped.")

def describe_table(table_name):
    if table_name in table_schemas:
        print(json.dumps(table_schemas[table_name], indent=2))
    else:
        print("Table does not exist.")
