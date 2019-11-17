import numpy
import pandas
import pprint
import pandas as pd
import numpy as np
import pyodbc
from db_creds import sqlserver_oltp
from db_creds import datawarehouse_db_config
from db_creds import datawarehouse_name

class emp_dim:

    def __init__(self):
        print(sqlserver_oltp)
        print("Enter credentials")
        print('connecting to EDW ')

    def db_query(self):
        query = 'select IIF(p.MiddleName IS NULL, p.firstname + p.lastname, p.firstname + ' '+ p.MiddleNAme + ' '+p.lastname) as [FullName] ' \
            ', e.BusinessEntityID , d.[Name], d.GroupName ' \
            'FROM HumanResources.Employee e JOIN Person.Person p on p.BusinessEntityID = e.BusinessEntityID ' \
            'JOIN HumanResources.EmployeeDepartmentHistory edh on edh.BusinessEntityID = e.BusinessEntityID ' \
            'JOIN HumanResources.Department d on d.DepartmentID = edh.DepartmentID'
        cnxn = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};SERVER='+'DATABASE='+self.database+'UID='+self.username+'PWD='+self.password)
        cursor = cnxn.cursor()
        print('Executing Query')
        result = cursor.execute(query)
        rows = cursor.fetchall()
        for x in rows:
            print(x[0:])
        cnxn.close()
        print('Connection to ' + self.host + '\nClosed')
    def dataframe_pd(self):
        query = 'SELECT sp.BusinessEntityID , p.LastName ,sp.SalesYTD  ,sp.SalesQuota, sp.salesYTD/SalesQuota as [Yearly_Achievement]'\
        'FROM Person.Person p JOIN Sales.SalesPerson sp on sp.BusinessEntityID = p.BusinessEntityID'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC DRIVER 17 for SQL SERVER};SERVER=' + self.host + 'DATABASE=' + self.database + 'UID=' + self.username + 'PWD=' + self.password)
        #execute data frame columns
        sql  = pd.read_sql_query(query, cnxn)
        df = pd.DataFrame(sql, columns=['BusinessEntityID', 'LastName', 'SalesYTD', 'SalesQuota', 'Yearly_Achievement'])
        print(df.agg)
        cnxn.close()
    def new_db_conn(self):
        target_cnx = pyodbc.connect(**datawarehouse_db_config)
        for config in datawarehouse_db_config:
            try:
                print("loading db: " + config['database'])
                #etl_process(sqlserver_queries, target_cnx, config, 'sqlserver')
            except Exception as error:
                print("etl for {} has error".format(config['database']))
                print('error message: {}'.format(error))

if __name__ == '__main__':
    localdb = emp_dim()
    #localdb.dataframe_pd()
    localdb.new_db_conn()