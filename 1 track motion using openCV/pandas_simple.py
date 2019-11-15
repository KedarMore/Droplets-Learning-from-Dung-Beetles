import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

#df = pd.DataFrame(data) 
  
# Declare a list that is to be converted into a column 
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
  
# Using 'Address' as the column name 
# and equating it to the list 
df['Address'] = address

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
