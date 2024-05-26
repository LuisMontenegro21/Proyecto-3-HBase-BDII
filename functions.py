from schemas import schemas, tables, table_status
import os, fastavro, json

'''Implement some extra functions that do not go with DDL or DML'''

def save_data():
    for table_name, table_data in tables.items():
        if table_name not in table_status or table_status[table_name] == 'enabled':
            with open(f"{table_name}.avro", 'wb') as f:
                fastavro.writer(f, table_data['schema'], table_data['records'])
            print(f"Data for table '{table_name}' saved to {table_name}.avro")

def load_data():
    for table_name, schema in schemas.items():
        if os.path.exists(f"{table_name}.avro"):
            with open(f"{table_name}.avro", 'rb') as f:
                records = list(fastavro.reader(f))
                tables[table_name] = {'schema': schema, 'records': records}
                table_status[table_name] = 'enabled'
            print(f"Data for table '{table_name}' loaded from {table_name}.avro")

def insert_record():
    table_name = input("Enter table name: ")
    if table_name in tables and table_status.get(table_name) == 'enabled':
        record = {}
        schema = tables[table_name]['schema']
        for field in schema['fields']:
            value = input(f"Enter value for {field['name']} ({field['type']}): ")
            if field['type'] == 'int':
                record[field['name']] = int(value)
            elif field['type'] == 'float':
                record[field['name']] = float(value)
            else:
                record[field['name']] = value
        tables[table_name]['records'].append(record)
        print(f"Record inserted into '{table_name}'.")
    elif table_name in tables and table_status.get(table_name) == 'disabled':
        print(f"Table '{table_name}' is disabled.")
    else:
        print("Table does not exist.")

def display_data():
    table_name = input("Enter table name: ")
    if table_name in tables:
        for record in tables[table_name]['records']:
            print(json.dumps(record, indent=2))
    else:
        print("Table does not exist.")