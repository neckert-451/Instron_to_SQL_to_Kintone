import pandas as pd
import numpy as np

# import csv file
df = pd.read_csv('SQL_export.csv')
print(df)

# rename headers
df.columns
print(df.columns)
df.columns = ['Parent_Id', 'd.Data_Tag_Id', 'Data_Float', 'Data_Int', 'Data_Text',
              'Related_Id', 'd.Datum_Column_Id', 'dco.Datum_Column_Id', 'dco.User_Label_Id',
              'dco.Data_Tag_Id', 'ul.User_Label_Id', 'Label', 'dca.Data_Tag_Id',
              'dca.Data_Category_Id', 'dca.Description', 'dt.Data_Category', 'dt.Description',
              'sa.Guid', 'Sample_Name', 'sp.Guid', 'sp.Sample_Id', 'Test_Id', 'Specimen_Id', 'Create_Date']
print(df.columns)
print(df)

# delete columns we don't need
df.pop('d.Data_Tag_Id')
df.pop('d.Datum_Column_Id')
df.pop('dco.Datum_Column_Id')
df.pop('dco.User_Label_Id')
df.pop('dco.Data_Tag_Id')
df.pop('ul.User_Label_Id')
df.pop('dca.Data_Tag_Id')
df.pop('dca.Data_Category_Id')
df.pop('dca.Description')
df.pop('dt.Data_Category')
df.pop('dt.Description')
df.pop('sa.Guid')
df.pop('sp.Guid')
df.pop('sp.Sample_Id')
print(df)

# delete rows where Sample Name is null
df = df.dropna(axis=0, subset=['Sample_Name'])
print(df)

# export to csv
df.to_csv('exported_data.csv')
