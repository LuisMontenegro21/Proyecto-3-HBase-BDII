from schemas import table_schemas, tables, table_status
import os, json

def create_table(table_name):
    if table_name not in tables:
        tables[table_name] = {"schema": {"namespace": "example.avro",
                                         "type": "record",
                                         "name": table_name,
                                         "fields": []},
                              "records": {}}
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
    if table_name in table_schemas:
        if table_status[table_name] == 'disabled':
            table_status[table_name] = 'enabled'
            print(f"Table '{table_name}' is now enabled.")
        else:
            print(f"Table '{table_name}' is already enabled.")
    else:
        print(f"Table: {table_name} does not exist.")

def alter_table(table_name):
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
        print(f"Table {table_name} does not exist.")

# TODO check correct functionality
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
    for table_name in list(tables.keys()):
        drop_table(table_name)
    print("All tables dropped.")

def describe_table(table_name):
    if table_name in tables:
        print(json.dumps(tables[table_name]['schema'], indent=2))
    else:
        print(f"Table {table_name} does not exist")
