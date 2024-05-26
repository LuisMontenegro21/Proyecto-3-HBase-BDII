from collections import defaultdict

schemas = {
    'employees': {
        "namespace": "example.avro",
        "type": "record",
        "name": "Employee",
        "fields": [
            {"name": "employee_id", "type": "int"},
            {"name": "first_name", "type": "string"},
            {"name": "last_name", "type": "string"},
            {"name": "department_id", "type": "int"},
            {"name": "email", "type": "string"},
            {"name": "hire_date", "type": "string"},
            {"name": "salary", "type": "float"},
            {"name": "position", "type": "string"}
        ]
    },
    'departments': {
        "namespace": "example.avro",
        "type": "record",
        "name": "Department",
        "fields": [
            {"name": "department_id", "type": "int"},
            {"name": "department_name", "type": "string"},
            {"name": "creation_date", "type": "string"},
            {"name": "manager_id", "type": "int"}
        ]
    },
    'projects': {
        "namespace": "example.avro",
        "type": "record",
        "name": "Project",
        "fields": [
            {"name": "project_id", "type": "int"},
            {"name": "project_name", "type": "string"},
            {"name": "start_date", "type": "string"},
            {"name": "end_date", "type": "string"}
        ]
    },
    'candidates': {
        "namespace": "example.avro",
        "type": "record",
        "name": "Candidate",
        "fields": [
            {"name": "candidate_id", "type": "int"},
            {"name": "first_name", "type": "string"},
            {"name": "last_name", "type": "string"},
            {"name": "department", "type": "string"},
            {"name": "status", "type": "string"},
            {"name": "email", "type": "string"}
        ]
    }
}

tables = {}
table_status = defaultdict(lambda: 'enabled')