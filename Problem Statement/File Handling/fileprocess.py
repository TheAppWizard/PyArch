import os

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print("An error occurred while reading the file:", e)
            return None

    def write_file(self, data):
        try:
            with open(self.file_path, 'w') as file:
                file.write(data)
                print("Data successfully written to the file.")
        except Exception as e:
            print("An error occurred while writing to the file:", e)

# Example usage:
file_path = "/Users/macbook/Desktop/Other Projects/PyArch/Problem Statement/File Handling/example.txt"
file_processor = FileProcessor(file_path)
file_processor.write_file("Hello, World!\nThis is a test.")
file_content = file_processor.read_file()
if file_content:
    print("File content:")
    print(file_content)
