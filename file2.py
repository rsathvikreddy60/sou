# file2.py

from file1 import read_data

def process_data():
    data = read_data()
    processed_data = data.upper()  # Just converting the string to uppercase as an example
    return processed_data

if __name__ == "__main__":
    print(process_data())
