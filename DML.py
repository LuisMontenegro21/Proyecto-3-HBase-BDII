from schemas import tables, table_status
from DDL import disable_table, drop_table, create_table
from functions import save_table
import time


def put_record():
    table_name = input("Insert table name: ")
    row_key = input("Insert row_key: ")
    column_family = input("Insert column_family: ")
    column_qualifier = input("Insert column_qualifier: ")
    value = input("Insert value: ")

    if table_name not in tables:
        print(f"Table '{table_name}' does not exist.")
        return

    if tables[table_name]['status'] == 'disabled':
        print(f"Table '{table_name}' is disabled.")
        return

    table = tables[table_name]
    timestamp = str(int(time.time() * 1000))  # Current timestamp in milliseconds
    version = 1

    # Initialize record if it doesn't exist
    if row_key not in table['records']:
        table['records'][row_key] = {}

    record = table['records'][row_key]

    if column_family not in table['schema']['column_families']:
        print(f"Column family '{column_family}' does not exist in table '{table_name}'.")
        return

    if column_family not in record:
        record[column_family] = {}

    if column_qualifier not in record[column_family]:
        record[column_family][column_qualifier] = []

    # Ensure we keep only the allowed number of versions
    max_versions = table['schema']['column_families'][column_family]['versions']
    if len(record[column_family][column_qualifier]) >= max_versions:
        record[column_family][column_qualifier].pop(0)  # Remove the oldest version

    # Add the new value with its timestamp and version
    record[column_family][column_qualifier].append({
        'value': value,
        'timestamp': timestamp,
        'version': version
    })

    save_table(table_name)
    print(f"Value '{value}' added to table '{table_name}' at row '{row_key}', column family '{column_family}', column qualifier '{column_qualifier}'.")






def get(table_name, row_key):
    if table_name in tables and table_status[table_name] == 'enabled':
        if row_key in tables[table_name]['records']:
            return tables[table_name]['records'][row_key]
        else:
            print(f"Row {row_key} does not exist in table {table_name}.")
    else:
        print("Table does not exist or is disabled.")
    return None


def scan(table_name):
    if table_name in tables and table_status[table_name] == 'enabled':
        return tables[table_name]['records']
    else:
        print("Table does not exist or is disabled.")
    return None


def delete(table_name, row_key, column_family, column):
    if table_name in tables and table_status[table_name] == 'enabled':
        if row_key in tables[table_name]['records'] and column_family in tables[table_name]['records'][row_key]:
            if column in tables[table_name]['records'][row_key][column_family]:
                del tables[table_name]['records'][row_key][column_family][column]
                print(f"Deleted column {column_family}:{column} from row {row_key} in table {table_name}.")
            else:
                print(f"Column {column_family}:{column} does not exist in row {row_key}.")
        else:
            print(f"Row {row_key} or column family {column_family} does not exist in table {table_name}.")
    else:
        print("Table does not exist or is disabled.")


def deleteall(table_name, row_key):
    if table_name in tables and table_status[table_name] == 'enabled':
        if row_key in tables[table_name]['records']:
            del tables[table_name]['records'][row_key]
            print(f"Deleted all columns from row {row_key} in table {table_name}.")
        else:
            print(f"Row {row_key} does not exist in table {table_name}.")
    else:
        print("Table does not exist or is disabled.")


def count(table_name):
    if table_name in tables and table_status[table_name] == 'enabled':
        row_count = len(tables[table_name]['records'])
        print(f"Table {table_name} has {row_count} rows.")
        return row_count
    else:
        print("Table does not exist or is disabled.")
    return 0



def truncate(table_name):
    if table_name in tables:
        disable_table(table_name)
        drop_table(table_name)
        create_table(table_name)
        print(f"Table {table_name} truncated.")
    else:
        print("Table does not exist.")
