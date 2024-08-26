import pandas as pd

# Load the Excel files
df1 = pd.read_excel('38th EACTS Annual Meeting-25-08-2024_06-56-26.xlsx', sheet_name='Test 1')
df2 = pd.read_excel('Aortic Valve Repair Summit-25-08-2024_06-45-50.xlsx', sheet_name='Test active members')

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
