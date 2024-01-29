import pandas as pd

def main():
    try:
        df = pd.read_excel("aset/asetEdomGjl2223.xlsx", sheet_name="Informatika")
        print(f"File loaded successfully! Sheet name: {"Informatika"}.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return
    except KeyError:
        print("Worksheet not found. Please check the worksheet name.")
        return

    # Find the first empty column
    next_empty_column = df.shape[1] + 1  # Columns start from 1 in pandas

    # Prompt for user confirmation
    set_title_confirmation = input("Yes = Enter title manually\nNo = Use default title:\n ").lower().strip()

    if set_title_confirmation == "yes":
        # Prompt for the title
        title = input("Enter the title: ")
    else:
        title = "Contoh"

    # Insert the title in the first row of the empty column
    df.loc[0, next_empty_column] = title
    print(f"Title inserted in column {next_empty_column}.")

    # Insert data in the next rows of the same column, starting from the second row
    df.loc[1:, next_empty_column] = "WorkSheet Title"  # Fill column with worksheet title
    print(f"Data inserted in column {next_empty_column}.")

    # Save the modified DataFrame to Excel
    df.to_excel("aset/asetEdomGjl2223.xlsx", index=False)  # Don't save index

if __name__ == "__main__":
    main()
