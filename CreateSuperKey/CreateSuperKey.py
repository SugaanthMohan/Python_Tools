#! /usr/bin/python3.5


import pandas as pd
import numpy as np

TableName = 'EmployeeDetails'
tableStructSuffix = '_TableStructure'

# READ THE TABLE STRUCTURE
table_features      = pd.read_csv(TableName + tableStructSuffix + '.csv' )

# GET THE KEYS LIST FROM YOUR TABLE STRUCUTRE
Table_Keys_List     = table_features[ ( table_features['Key'].isna() == False ) & (table_features['Type'] != 'timestamp') ]['Field'].values.tolist()

# READ THE DATA FOR THE EMPLOYEE DETAILS
dataset = pd.read_csv( TableName + '.csv' )

# CREATE THE SUPER KEY BY JOINING THE KEYS LIST WITH A DELIMITER '|' (PIPE SYMBOL)
dataset['SUPERKEY'] = dataset[Table_Keys_List].applymap(str).apply(lambda x: '|'.join(x), axis=1)
