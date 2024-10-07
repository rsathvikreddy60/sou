# file3.py

from file2 import process_data

def analyze_data():
    processed_data = process_data()
    analysis_result = len(processed_data.split())  # Example: Count the number of words
    return analysis_result

if __name__ == "__main__":
    print(f"Number of words: {analyze_data()}")
