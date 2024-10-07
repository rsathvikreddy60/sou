# file4.py

from file3 import analyze_data

def save_result():
    analysis_result = analyze_data()
    with open('result.txt', 'w') as f:
        f.write(f"Analysis Result: {analysis_result} words")
    print(f"Result saved to result.txt: {analysis_result} words")

if __name__ == "__main__":
    save_result()
