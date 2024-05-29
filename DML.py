from schemas import tables, table_status
from DDL import disable_table, drop_table, create_table

import time

def put(table_name, row_key, column_family, column, value):
    if table_name in tables and table_status[table_name] == 'enabled':
        timestamp = int(time.time())
        if row_key not in tables[table_name]['records']:
            tables[table_name]['records'][row_key] = {}
        if column_family not in tables[table_name]['records'][row_key]:
            tables[table_name]['records'][row_key][column_family] = {}
        tables[table_name]['records'][row_key][column_family][column] = (timestamp, value)
        print(f"Inserted value in {table_name}: {row_key}, {column_family}:{column} = {value}")
    else:
        print("Table does not exist or is disabled.")



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
