import pprint
import pandas as pd
import numpy as np
import pyodbc
#this script connects to Microsoft SQL database.
#In one method it creates a data frame the other method (db_query) just pulls data with cursor
class db:
    #constructor with db credentials...you can change this to your database
    #or download Microsoft AdventureWorks2016 Database online (OLTP) one.
    def __init__(self):
        print("Enter credentials")
        print('connecting to EDW ')
        self.host = 'DESKTOP-03RVSDU\steven;'
        self.database =  'AdventureWorks2016;'
        self.username = 'sguri002;'
        self.password ='#!Micheal12;'
    #Pulls data from Adventure Works 2016 Database but does not create a data frame.
    def db_query(self):
        #string containing query
        query = 'select IIF(p.MiddleName IS NULL, p.firstname + p.lastname, p.firstname + ' '+ p.MiddleNAme + ' '+p.lastname) as [FullName] ' \
            ', e.BusinessEntityID , d.[Name], d.GroupName ' \
            'FROM HumanResources.Employee e JOIN Person.Person p on p.BusinessEntityID = e.BusinessEntityID ' \
            'JOIN HumanResources.EmployeeDepartmentHistory edh on edh.BusinessEntityID = e.BusinessEntityID ' \
            'JOIN HumanResources.Department d on d.DepartmentID = edh.DepartmentID'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.host+"DATABASE="+self.database+"UID="+self.username+"PWD="+self.password)
        #Creates cursor for connection
        cursor = cnxn.cursor()
        print('Executing Query')
        result = cursor.execute(query) #go one by one
        rows = cursor.fetchall() # get all data from query at once.
        for x in rows:
            #notation to show index 0 to n.
            print(x[0:])
        cnxn.close()
        print('Connection to ' + self.host + '\nClosed')

    #creates a data frame from a query using pandas library.
    #data is pulled from adventure works.
    def dataframe_pd(self):
        print('DateFrame Using Pandas lib')
        query = 'SELECT sp.BusinessEntityID , p.LastName ,sp.SalesYTD  ,sp.SalesQuota, sp.salesYTD/SalesQuota as [Current Achievement]'\
        'FROM Person.Person p JOIN Sales.SalesPerson sp on sp.BusinessEntityID = p.BusinessEntityID'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC DRIVER 17 for SQL SERVER}; SERVER=' + self.host + 'DATABASE=' + self.database + 'UID=' + self.username + 'PWD=' + self.password)
        #execute data frame columns
        sql  = pd.read_sql_query(query, cnxn)
        df = pd.DataFrame(sql, columns=['BusinessEntityID', 'LastName', 'SalesYTD', 'SalesQuota', 'Yearly_Achievement'])
        print(df)
        cnxn.close()

#main method
if __name__ == '__main__':
    localdb = db()
    localdb.db_query()
    localdb.dataframe_pd()