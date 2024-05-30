from schemas import table_schemas, tables, table_status
from functions import initialize_tables, save_table_metadata, save_table
import os, json, shutil

# we initialize the tables from the data before modifying it
initialize_tables()

# get column families from the user. It specifies which column families the table will have and number of versions
def get_column_families_from_user():
    column_families = {}
    while True:
        cf_name = input("Enter column family name (or 'done' to finish): ")
        if cf_name.lower() == 'done':
            break
        versions = input(f"Enter the number of versions for column family '{cf_name}' (default is 3): ")
        try:
            versions = int(versions) if versions else 3
        except ValueError:
            print("Invalid number of versions. Using default value of 3.")
            versions = 3
        column_families[cf_name] = {"versions": versions}
    return column_families

# creates the new table in base of the column families given
def create_table():

    table_name = input("Enter table name: ")
    column_families = get_column_families_from_user()

    if not column_families:
        print("No column families defined. Table creation aborted.")
        return

    # Construct the schema with necessary Avro properties
    schema = {
        "namespace": f"com.companyname.{table_name}",
        "type": "record",
        "name": table_name,
        "fields": [
            {"name": "row_key", "type": "string"},
            {"name": "timestamp", "type": "string"},
            {"name": "version", "type": "int"}
        ],
        "column_families": column_families
    }

    # Add the table schema to the global tables dictionary
    if table_name not in tables:
        tables[table_name] = {
            "schema": schema,
            "records": [],
            "status": "enabled"
        }
        os.makedirs(f"data/{table_name}", exist_ok=True)
        print(f"Table '{table_name}' created successfully.")
    else:
        print(f"Table '{table_name}' already exists.")
    
    save_table(table_name)

# lists all the tables available and their status
def list_tables():
    if tables:
        print("Tables:")
        for table_name, table_info in tables.items():
            status = table_info.get("status", "enabled")
            print(f"- {table_name} ({status})")
    else:
        print("There are no tables")

# disables a table 
def disable_table():
    table_name = input("Input the table name: ")
    if table_name in tables:
        tables[table_name]['status'] = 'disabled'
        save_table_metadata(table_name)
        print(f"Table '{table_name}' is now disabled.")
    else:
        print(f"Table '{table_name}' does not exist.")

# enables a table if disabled
def enable_table():
    table_name = input("Input the table name: ")
    if table_name in tables:
        if tables[table_name]['status'] == 'disabled':
            tables[table_name]['status'] = 'enabled'
            save_table_metadata(table_name)
            print(f"Table '{table_name}' is now enabled.")
        else:
            print(f"Table '{table_name}' is already enabled.")
    else:
        print(f"Table '{table_name}' does not exist.")

# drops a table in case this one is previously disabled, else it does not
def drop_table():

    table_name = input("Input table name to drop: ")

    if table_name in tables:
        if tables[table_name]['status'] == 'disabled':
            table_dir = os.path.join("data", table_name)
            if os.path.exists(table_dir):
                shutil.rmtree(table_dir)  # Remove the entire directory and its contents
            del tables[table_name]
            print(f"Table '{table_name}' dropped successfully.")
        else:
            print(f"Table '{table_name}' is not disabled. Please disable the table before dropping it.")
    else:
        print(f"Table '{table_name}' does not exist.")

# describes a table
def describe_table():

    table_name = input("Input the name of the table: ")
    if table_name in tables:
        table = tables[table_name]
        schema = table['schema']
        status = table['status']
        print(f"Table '{table_name}' description:")
        print(json.dumps(schema, indent=2))
        print(f"Status: {status}")
    else:
        print(f"Table '{table_name}' does not exist.")

# drops all tables currently disabled 
# TODO give a param to be more specific of which ones to delete
def drop_all():

    tables_to_drop = list(tables.keys())
    for table_name in tables_to_drop:
        if tables[table_name]['status'] == 'disabled':
            drop_table(table_name)
        else:
            print(f"Table '{table_name}' is not disabled. Please disable the table before dropping it.")

# alters a table by removing or adding column families and versions
def alter_table():

    table_name = input("Enter the table name to alter: ")

    if table_name not in tables:
        print(f"Table '{table_name}' does not exist.")
        return

    print("Choose an operation:")
    print("1. Add Column Family")
    print("2. Delete Column Family")
    print("3. Modify Column Family Versions")
    operation = input("Enter the operation number: ")

    if operation == "1":
        add_column_family(table_name)
    elif operation == "2":
        delete_column_family(table_name)
    elif operation == "3":
        modify_column_family_versions(table_name)
    else:
        print("Invalid operation.")

# adds new column family
def add_column_family(table_name):

    cf_name = input("Enter the new column family name: ")
    if cf_name in tables[table_name]['schema']['column_families']:
        print(f"Column family '{cf_name}' already exists.")
        return
    
    versions = input(f"Enter the number of versions for column family '{cf_name}' (default is 1): ")
    try:
        versions = int(versions) if versions else 1
    except ValueError:
        print("Invalid number of versions. Using default value of 1.")
        versions = 1

    tables[table_name]['schema']['column_families'][cf_name] = {"versions": versions}
    save_table_metadata(table_name)
    save_table(table_name)
    print(f"Column family '{cf_name}' added to table '{table_name}'.")

# removes an existing column family
def delete_column_family(table_name):

    cf_name = input("Enter the column family name to delete: ")
    if cf_name not in tables[table_name]['schema']['column_families']:
        print(f"Column family '{cf_name}' does not exist.")
        return

    del tables[table_name]['schema']['column_families'][cf_name]
    save_table_metadata(table_name)
    save_table(table_name)
    print(f"Column family '{cf_name}' deleted from table '{table_name}'.")

# changes the number of versions a column family has
def modify_column_family_versions(table_name):

    cf_name = input("Enter the column family name to modify: ")
    if cf_name not in tables[table_name]['schema']['column_families']:
        print(f"Column family '{cf_name}' does not exist.")
        return

    versions = input(f"Enter the new number of versions for column family '{cf_name}': ")
    try:
        versions = int(versions)
    except ValueError:
        print("Invalid number of versions. Operation aborted.")
        return

    tables[table_name]['schema']['column_families'][cf_name]['versions'] = versions
    
    save_table_metadata(table_name)
    save_table(table_name)
    print(f"Number of versions for column family '{cf_name}' in table '{table_name}' updated to {versions}.")

# saves changes to the metadada json
def save_table_metadata(table_name):
    if table_name in tables:
        table = tables[table_name]
        metadata = {
            "status": table['status'],
            "schema": table['schema']
        }
        with open(f"data/{table_name}/metadata.json", 'w') as metadata_file:
            json.dump(metadata, metadata_file)
