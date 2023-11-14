import os
import pandas as pd


class FileConverter:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory
        os.makedirs(output_directory, exist_ok=True)

    def convert_file(self, file):
        file_path = os.path.join(self.input_directory, file)
        df = self._read_file(file_path)
        output_file_path = os.path.join(
            self.output_directory, os.path.splitext(file)[0] + ".json"
        )
        self._save_to_json(df, output_file_path)

    def _read_file(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() in (".xls", ".xlsx", ".xlsm", ".xlsb"):
            return pd.read_excel(file_path)
        elif file_extension.lower() == ".ods":
            return pd.read_excel(file_path, engine="odf")
        elif file_extension.lower() == ".csv":
            return pd.read_csv(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

    def _save_to_json(self, df, output_file_path):
        df.to_json(output_file_path, orient="records")
