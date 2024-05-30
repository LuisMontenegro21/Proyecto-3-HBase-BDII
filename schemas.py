from collections import defaultdict



table_schemas = {
    'employees': {
        "namespace": "com.companyname.hr.employees",
        "type": "record",
        "name": "Employee",
        "fields": [
            {"name": "employee_id", "type": "int"},
            {"name": "personal:first_name", "type": "string"},
            {"name": "personal:last_name", "type": "string"},
            {"name": "employment:department_id", "type": "int"},
            {"name": "personal:email", "type": "string"},
            {"name": "employment:hire_date", "type": "string"},
            {"name": "employment:salary", "type": "float"},
            {"name": "employment:position", "type": "string"},
            {"name": "employment:department_name", "type": "string"},
            {"name": "employment:creation_date", "type": "string"},
            {"name": "projects:project_1", "type": "string"},
            {"name": "projects:project_2", "type": "string"}
        ]
    },
    'departments': {
        "namespace": "com.companyname.hr.departments",
        "type": "record",
        "name": "Department",
        "fields": [
            {"name": "department_id", "type": "int"},
            {"name": "info:department_name", "type": "string"},
            {"name": "info:creation_date", "type": "string"},
            {"name": "manager:manager_id", "type": "int"},
            {"name": "manager:manager_name", "type": "string"}
        ]
    },
    'projects': {
        "namespace": "com.companyname.hr.projects",
        "type": "record",
        "name": "Project",
        "fields": [
            {"name": "project_id", "type": "int"},
            {"name": "info:project_name", "type": "string"},
            {"name": "info:start_date", "type": "string"},
            {"name": "info:finish_date", "type": "string"}
        ]
    },
    'candidates': {
        "namespace": "com.companyname.hr.candidates",
        "type": "record",
        "name": "Candidate",
        "fields": [
            {"name": "candidate_id", "type": "int"},
            {"name": "personal:first_name", "type": "string"},
            {"name": "personal:last_name", "type": "string"},
            {"name": "personal:email", "type": "string"},
            {"name": "application:department", "type": "string"},
            {"name": "application:status", "type": "string"}
        ]
    }
}


tables = {}
table_status = defaultdict(lambda: 'enabled')


