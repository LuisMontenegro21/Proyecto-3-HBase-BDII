from schemas import table_schemas, tables, table_status
import os, json, avro.schema, avro.datafile, avro.io

employee_avro_schema = avro.schema.Parse(json.dumps(table_schemas["employees"]))
departments_avro_schema = avro.schema.Parse(json.dumps(table_schemas["departments"]))
projects_avro_schema = avro.schema.Parse(json.dumps(table_schemas["projects"]))
candidates_avro_schema = avro.schema.Parse(json.dumps(table_schemas["candidates"]))

def save_table(table_name):
    if table_name in tables:
        schema = avro.schema.Parse(json.dumps(tables[table_name]['schema']))
        with open(f"data/{table_name}/data.avro", 'wb') as f:
            writer = avro.datafile.DataFileWriter(f, avro.io.DatumWriter(), schema)
            for record in tables[table_name]['records']:
                writer.append(record)
            writer.close()
        print(f"Data for table '{table_name}' saved to 'data/{table_name}/data.avro'.")
    else:
        print(f"Table '{table_name}' does not exist.")

def load_table(table_name):
    if table_name in tables:
        schema = avro.schema.Parse(json.dumps(tables[table_name]['schema']))
        if os.path.exists(f"data/{table_name}/data.avro"):
            with open(f"data/{table_name}/data.avro", 'rb') as f:
                reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())
                records = [record for record in reader]
                tables[table_name]['records'] = records
                reader.close()
            print(f"Data for table '{table_name}' loaded from 'data/{table_name}/data.avro'.")
        else:
            print(f"No data file found for table '{table_name}'.")
    else:
        print(f"Table '{table_name}' does not exist.")

def insert_record(table_name):
    if table_name in tables and table_status.get(table_name) == 'enabled':
        record = {}
        schema = tables[table_name]['schema']
        for field in schema['fields']:
            value = input(f"Enter value for {field['name']} ({field['type']}): ")
            try:
                if field['type'] == 'int':
                    record[field['name']] = int(value)
                elif field['type'] == 'float':
                    record[field['name']] = float(value)
                else:
                    record[field['name']] = value
            except ValueError:
                print(f"Invalid value for {field['name']} ({field['type']}).")
                return
        tables[table_name]['records'].append(record)
        print(f"Record inserted into '{table_name}'.")
    elif table_name in tables and table_status.get(table_name) == 'disabled':
        print(f"Table '{table_name}' is disabled.")
    else:
        print("Table does not exist.")

def display_data(table_name):
    if table_name in tables:
        for record in tables[table_name]['records']:
            print(json.dumps(record, indent=2))
    else:
        print("Table does not exist.")

