# Comparing two Excel sheets using Python and pandas involves a few steps

Step-by-Step process :-

1. Install the python(Using microsoft store or https://www.python.org/downloads/)
2. Install the required libraries
```
pip install pandas
pip install openpyxl
```
3. Create a python script file in VS code(Eg: compare_excel.py)
4. Add the below code in **compare_excel.py** file
```ruby
import pandas as pd
# Load the Excel files
df1 = pd.read_excel('path_to_file1.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel('path_to_file2.xlsx', sheet_name='Sheet1')

# Compare the DataFrames
if df1.equals(df2):
    print("The sheets are equal.")
else:
    print("The sheets are not equal.")
    # Optional: Save differences
    diff1 = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
    diff2 = df2[~df2.apply(tuple, 1).isin(df1.apply(tuple, 1))]

    with pd.ExcelWriter('comparison_report.xlsx') as writer:
        diff1.to_excel(writer, sheet_name='In_df1_not_in_df2')
        diff2.to_excel(writer, sheet_name='In_df2_not_in_df1')
```
5. Add your excel file name in

    **path_to_file1.xlsx = examplefile_01.xlsx and 
   Path_to_file2.xlsx = examplefile_02.xlsx**

7. Add you sheet name in
   
    **Sheet1 = examplefilesheet_1 and 
      Sheet1 = examplefilesheet_2**
   
9. Run the Python script

```
python compare_excel.py
```

8. Example code ;-

```ruby
import pandas as pd
# Load the Excel files
df1 = pd.read_excel('examplefile_01.xlsx', sheet_name='examplefilesheet_1')
df2 = pd.read_excel('examplefile_02.xlsx', sheet_name='examplefilesheet_2')

# Compare the DataFrames
if df1.equals(df2):
    print("The sheets are equal.")
else:
    print("The sheets are not equal.")
    # Optional: Save differences
    diff1 = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
    diff2 = df2[~df2.apply(tuple, 1).isin(df1.apply(tuple, 1))]

    with pd.ExcelWriter('comparison_report.xlsx') as writer:
        diff1.to_excel(writer, sheet_name='In_df1_not_in_df2')
        diff2.to_excel(writer, sheet_name='In_df2_not_in_df1')
```
   
