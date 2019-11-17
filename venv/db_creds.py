from variables import datawarehouse_name
from variables import sql_source_db
# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
    'Trusted_Connection': 'yes',
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': 'DESKTOP-03RVSDU\steven',
    'database': '{}'.format(datawarehouse_name),
    'user': 'sguri002',
    'password': '#!Micheal12',
    'autocommit': True,
    }
# Staging DB fro DWH
staging_db_config = [{
        'Trusted_Connection': 'yes',
        'driver': '{ODBC Driver 17 for SQL Server}',
        'server': 'DESKTOP-03RVSDU\steven',
        'database': '{}'.format(sql_source_db),
        'user': 'sguri002',
        'password': '#!Micheal12',
        'autocommit': True,
    }]
# sql-server (source db)
sqlserver_oltp = [{
        'Trusted_Connection': 'yes',
        'driver': 'ODBC Driver 17 for SQL Server}',
        'server': 'DESKTOP-03RVSDU\steven',
        'database': '{}'.format(sql_source_db),
        'user': 'sguri002',
        'password': '#!Micheal12',
        'autocommit': True,
    }]