import unittest
from modules.file_converter import FileConverter
import os
import pandas as pd

class TestFileConverter(unittest.TestCase):
    def setUp(self):
        self.input_directory = "test_data/input"
        self.output_directory = "test_data/output"
        os.makedirs(self.input_directory, exist_ok=True)
        os.makedirs(self.output_directory, exist_ok=True)

        # Create some test files
        self.create_test_file("file1.xlsx", pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
        self.create_test_file("file2.csv", pd.DataFrame({"X": ["a", "b"], "Y": ["c", "d"]}))

        # Create an instance of FileConverter to use in tests
        self.file_converter = FileConverter(self.input_directory, self.output_directory)

    def tearDown(self):
        # Remove test files and directories
        for file in os.listdir(self.input_directory):
            file_path = os.path.join(self.input_directory, file)
            os.remove(file_path)
        os.rmdir(self.input_directory)

        for file in os.listdir(self.output_directory):
            file_path = os.path.join(self.output_directory, file)
            os.remove(file_path)
        os.rmdir(self.output_directory)

    def test_convert_file_excel(self):
        input_file = "file1.xlsx"
        self.file_converter.convert_file(input_file)
        output_file = os.path.join(self.output_directory, "file1.json")
        self.assertTrue(os.path.isfile(output_file), f"The output file {output_file} does not exist.")

    def test_convert_file_csv(self):
        input_file = "file2.csv"
        self.file_converter.convert_file(input_file)
        output_file = os.path.join(self.output_directory, "file2.json")
        self.assertTrue(os.path.isfile(output_file), f"The output file {output_file} does not exist.")

    def create_test_file(self, filename, data):
        file_path = os.path.join(self.input_directory, filename)
        if filename.endswith('.xlsx'):
            data.to_excel(file_path, index=False)
        elif filename.endswith('.csv'):
            data.to_csv(file_path, index=False)

if __name__ == '__main__':
    unittest.main()
