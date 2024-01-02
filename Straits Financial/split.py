import pandas as pd
import os

def split_large_file(input_file_path, output_folder):
    # Read the large CSV file with a header
    df = pd.read_csv(input_file_path, header=True)

    # Group the DataFrame by the C, D columns
    grouped = df.groupby(['CCC','eee'])


    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through groups and create separate files
    for c_value, group_df in grouped:
        # Create a filename based on the values in the C, D columns
        filename = f"{c_value}.csv"
        output_path = os.path.join(output_folder, filename)

        # Write the group to a separate Excel file
        group_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Specify the path to the input CSV file and the output folder
    input_file_path = "Main File for Splitting.csv"
    output_folder = "D:/splitting/"

    # Call the function to split the large file
    split_large_file(input_file_path, output_folder)
