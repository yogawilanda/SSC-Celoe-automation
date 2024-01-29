import pandas as pd

filename = 'aset/asetEdomGanjil2223.xlsx'
xl = pd.ExcelFile(filename)

# Get sheet names
get_sheet_names = xl.sheet_names

# Store the headers for each sheet in a dictionary
sheet_headers = {}

header = None

def read_first_row():
    # Loop through each sheet name
    for get_sheet_name in xl.sheet_names:
        # Read the first row (header) from the current sheet
        header = xl.parse(get_sheet_name, rows=1, header=None).values[0]
        # Store the header in the dictionary
        sheet_headers[get_sheet_name] = header
    
    # Access the headers for each sheet
    print("Headers for each sheet:")
    for get_sheet_name, header in sheet_headers.items():
        print(f"{get_sheet_name}: {header}")
        
def read_data():
    # Loop through each sheet name
    for get_sheet_name in xl.sheet_names:
        # Read the data from the current sheet starting from row 2
        data = xl.parse(get_sheet_name, skiprows=[0])
        
        # Print the data
        print(f"\n{get_sheet_name}:\n{data}")
        
def read_data_with_header():
    # Loop through each sheet name
    for get_sheet_name in xl.sheet_names:
        # Read the data from the current sheet starting from row 2
        data = xl.parse(get_sheet_name, skiprows=[0])
        # Print the data
        print(f"\n{get_sheet_name}:\n{data}")

def get_data_types_and_column(df):
    for sheet_name in xl.sheet_names:
        # Read the entire sheet
        df = xl.parse(sheet_name)
        print(f"Sheet: {sheet_name}\n\nColumns and Data Types:\n", df.dtypes, df.columns)


# read_first_row()
