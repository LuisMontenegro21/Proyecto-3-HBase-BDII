from collections import defaultdict
predefined_schemas = {
    "employees": [
        {"name": "employee_id", "type": "int"},
        {"name": "first_name", "type": "string"},
        {"name": "last_name", "type": "string"},
        {"name": "department_id", "type": "int"},
        {"name": "email", "type": "string"},
        {"name": "hire_date", "type": "string"},
        {"name": "salary", "type": "float"},
        {"name": "position", "type": "string"}
    ],
    "departments": [
        {"name": "department_id", "type": "int"},
        {"name": "department_name", "type": "string"},
        {"name": "creation_date", "type": "string"},
        {"name": "manager_id", "type": "int"}
    ],
    "projects": [
        {"name": "project_id", "type": "int"},
        {"name": "project_name", "type": "string"},
        {"name": "start_date", "type": "string"},
        {"name": "end_date", "type": "string"}
    ],
    "candidates": [
        {"name": "candidate_id", "type": "int"},
        {"name": "first_name", "type": "string"},
        {"name": "last_name", "type": "string"},
        {"name": "department", "type": "string"},
        {"name": "status", "type": "string"},
        {"name": "email", "type": "string"}
    ]
}

table_schemas = {
    'employees': {
        "namespace": "com.companyname.hr.employees",
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
        "namespace": "com.companyname.hr.departments",
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
        "namespace": "com.companyname.hr.projects",
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
        "namespace": "com.companyname.hr.candidates",
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


