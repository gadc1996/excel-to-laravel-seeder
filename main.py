import os
import pandas as pd

input_directory = "files"
output_directory = "dist"

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get a list of all files in the input directory
files = os.listdir(input_directory)

# Iterate through each file
for file in files:
    # Get the file path
    file_path = os.path.join(input_directory, file)

    # Check if the file is in Excel, ODS, or CSV format
    if file.lower().endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
        # Read Excel file
        df = pd.read_excel(file_path)
    elif file.lower().endswith('.ods'):
        # Read ODS file
        df = pd.read_excel(file_path, engine='odf')
    elif file.lower().endswith('.csv'):
        # Read CSV file
        df = pd.read_csv(file_path)
    else:
        # Skip files that are not Excel, ODS, or CSV
        continue

    # Generate output file path with the new extension
    output_file_path = os.path.join(output_directory, os.path.splitext(file)[0] + ".json")

    # Save DataFrame to JSON format in the output directory
    df.to_json(output_file_path, orient='records')

print("Conversion completed successfully.")
