from collections import Counter
import nltk
from nltk.tokenize import word_tokenize


f_name = "file.txt.txt"

def readfile(f_name):
    with open(f_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def tokenize(lines):
    words = []
    for line in lines:
        words.extend(word_tokenize(line.lower()))
    return words

def wordscounter(words):
    counts = Counter(words)
    return counts

r_name = "result.txt"

def writewordscount(counts, r_name):
    with open(r_name, "w", encoding="utf-8") as f:
        for word, count in counts.items():
            f.write(f"{word}: {count}\n")

def main(f_name, r_name):
    try:
        lines = readfile(f_name)
        words = tokenize(lines)
        word_counts = wordscounter(words)
        writewordscount(word_counts, r_name)
        print("Processing complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
main(f_name, r_name)
