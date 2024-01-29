import pandas as pd

def insert_empty_column_with_sheet_name(filename, sheet_name):
    """
    Inserts an empty column with the sheet name in the next available empty column.

    Args:
        filename (str): The path to the Excel file.
        sheet_name (str): The name of the sheet to process.
    """

    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:  # Open in append mode
        # Read the existing DataFrame
        df = pd.read_excel(filename, sheet_name=sheet_name)

        # Find the index of the next empty column (handling potential errors)
        try:
            next_empty_column = next(col for col in df.columns if df[col].isnull().all())
        except StopIteration:
            next_empty_column = len(df.columns)  # Append if no empty column found

        # Insert the empty column with the sheet name
        df.insert(loc=next_empty_column, column=sheet_name, value=pd.NA)

        # Write the modified DataFrame back to the Excel file
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Example usage:
filename = './aset/asetEdomGjl2223.xlsx'
sheet_name = "your_actual_sheet_name"  # Replace with the actual sheet name
insert_empty_column_with_sheet_name(filename, sheet_name)
