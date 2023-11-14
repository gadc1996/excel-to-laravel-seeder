import os
from modules.file_converter import FileConverter

input_directory = "data/input"
output_directory = "data/output"

file_converter = FileConverter(input_directory, output_directory)

files = os.listdir(input_directory)
for file in files:
    file_converter.convert_file(file)

print("Conversion completed successfully.")
