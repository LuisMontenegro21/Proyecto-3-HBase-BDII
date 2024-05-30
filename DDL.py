from schemas import table_schemas, tables, table_status, predefined_schemas
import os, json

def get_fields_from_user():
    fields = []
    while True:
        field_name = input("Enter field name (or 'done' to finish): ")
        if field_name.lower() == 'done':
            break
        field_type = input("Enter field type (int, string, float): ")
        if field_type in ['int', 'string', 'float']:
            fields.append({"name": field_name, "type": field_type})
        else:
            print("Invalid field type. Please enter 'int', 'string', or 'float'.")
    return fields

def create_table(table_name, module_name=None, namespace=None):
    if table_name in predefined_schemas:
        fields = predefined_schemas[table_name]
    else:
        print(f"No predefined schema for table '{table_name}'. Please define fields manually.")
        fields = get_fields_from_user()
        if not fields:
            print("No fields defined. Table creation aborted.")
            return

    if module_name:
        namespace = get_namespace(table_name)
    elif namespace is None:
        namespace = input("Enter namespace: ")
    
    if table_name not in tables:
        tables[table_name] = {
            "schema": {
                "namespace": namespace,
                "type": "record",
                "name": table_name,
                "fields": fields
            },
            "records": []
        }
        table_status[table_name] = 'enabled'
        os.makedirs(f"data/{table_name}", exist_ok=True)
        print(f"Table '{table_name}' created successfully.")
    else:
        print(f"Table '{table_name}' already exists.")

def list_tables():
    if tables:
        print("Tablas:")
        for table_name, status in table_status.items():
            print(f"- {table_name} ({status})")
    else:
        print("There are no tables")

def disable_table(table_name):
    if table_name in tables:
        table_status[table_name] = 'disabled'
        print(f"Table '{table_name}' is now disabled.")
    else:
        print(f"Table {table_name} does not exist")

def is_enabled(table_name):
    if table_name in tables:
        if table_status[table_name] == 'disabled':
            table_status[table_name] = 'enabled'
            print(f"Table '{table_name}' is now enabled.")
        else:
            print(f"Table '{table_name}' is already enabled.")
    else:
        print(f"Table: {table_name} does not exist.")

def alter_table(table_name):
    if table_name in tables:
        if table_status[table_name] == 'disabled':
            print(f"Table '{table_name}' is disabled. Operation cancelled.")
            return

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
        print(f"Table '{table_name}' does not exist.")


def drop_table(table_name):
    if table_name in table_schemas:
        region_dir = f"data/{table_name}"
        if os.path.exists(region_dir):
            for root, dirs, files in os.walk(region_dir):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(region_dir)
        del tables[table_name]
        del table_status[table_name]
        print(f"Table '{table_name}' dropped.")
    else:
        print(f"Table {table_name} does not exist")


def drop_all_tables():
    accept = str(input("Are you sure you want to delete all tables? : y/n"))
    if accept == 'y':
        for table_name in list(tables.keys()):
            drop_table(table_name)
        print("All tables dropped.")
    elif accept == 'n':
        print("Drop all tables canceled")
    else:
        print("Invalid command")

def describe_table(table_name):
    if table_name in tables:
        print(json.dumps(tables[table_name]['schema'], indent=2))
    else:
        print(f"Table {table_name} does not exist")

def get_namespace(table_name):
    return f"com.companyname.hr.{table_name}"