from schemas import table_schemas, tables, table_status
import os, json, avro.schema, avro.datafile, avro.io, time

employee_avro_schema = avro.schema.Parse(json.dumps(table_schemas["employees"]))
departments_avro_schema = avro.schema.Parse(json.dumps(table_schemas["departments"]))
projects_avro_schema = avro.schema.Parse(json.dumps(table_schemas["projects"]))
candidates_avro_schema = avro.schema.Parse(json.dumps(table_schemas["candidates"]))

def save_table(table_name):
    if table_name in tables:
        table = tables[table_name]
        schema = table['schema']
        records = table['records']
        status = table['status']
        schema_json = json.dumps(schema)

        # Save schema
        with open(f"data/{table_name}/schema.avsc", 'w') as schema_file:
            schema_file.write(schema_json)

        # Save records
        with open(f"data/{table_name}/data.avro", 'wb') as data_file:
            writer = avro.datafile.DataFileWriter(data_file, avro.io.DatumWriter(), avro.schema.Parse(schema_json))
            for record in records:
                writer.append(record)
            writer.close()

        # Save metadata
        metadata = {
            "status": status
        }
        with open(f"data/{table_name}/metadata.json", 'w') as metadata_file:
            json.dump(metadata, metadata_file)

        print(f"Data for table '{table_name}' saved to 'data/{table_name}/data.avro'.")
    else:
        print(f"Table '{table_name}' does not exist.")




def save_table_metadata(table_name):
    if table_name in tables:
        table = tables[table_name]
        metadata = {
            "status": table['status']
        }
        with open(f"data/{table_name}/metadata.json", 'w') as metadata_file:
            json.dump(metadata, metadata_file)

def initialize_tables():
    """
    Initializes the global tables dictionary by loading existing tables from disk.
    """
    global tables
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        return

    for table_name in os.listdir(data_dir):
        table_dir = os.path.join(data_dir, table_name)
        schema_file = os.path.join(table_dir, "schema.avsc")
        data_file = os.path.join(table_dir, "data.avro")
        metadata_file = os.path.join(table_dir, "metadata.json")

        if os.path.exists(schema_file) and os.path.exists(data_file) and os.path.exists(metadata_file):
            with open(schema_file, 'r') as sf:
                schema_json = sf.read()
                schema = json.loads(schema_json)

            records = []
            with open(data_file, 'rb') as df:
                reader = avro.datafile.DataFileReader(df, avro.io.DatumReader())
                for record in reader:
                    records.append(record)
                reader.close()

            with open(metadata_file, 'r') as mf:
                metadata = json.load(mf)
                status = metadata.get("status", "enabled")

            tables[table_name] = {
                "schema": schema,
                "records": records,
                "status": status
            }



def display_data(table_name):
    if table_name in tables:
        if table_status.get(table_name) == 'enabled':
            for record in tables[table_name]['records']:
                print(json.dumps(record, indent=2))
        elif table_status.get(table_name) == 'disabled':
            print(f"Table '{table_name}' is disabled.")
    else:
        print("Table does not exist.")

