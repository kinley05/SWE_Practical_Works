import string
from collections import Counter

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    return len(content.split())

def clean_words(content):
    return content.translate(str.maketrans('', '', string.punctuation)).lower().split()

def most_common_word(content):
    words = clean_words(content)
    word_counts = Counter(words)
    return word_counts.most_common(1)[0] if word_counts else ("None", 0)

def count_unique_words(content):
    words = set(clean_words(content))
    return len(words)

def find_longest_word(content):
    words = clean_words(content)
    return max(words, key=len) if words else ""

def count_specific_word(content, specific_word):
    words = clean_words(content)
    return words.count(specific_word.lower())

def average_word_length(content):
    words = clean_words(content)
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

def percentage_longer_than_average(content):
    words = clean_words(content)
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100 if words else 0

def analyze_text(filename, specific_word=None):
    content = read_file(filename)
    
    if not content:
        return  

    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, common_count = most_common_word(content)
    unique_word_count = count_unique_words(content)
    longest_word = find_longest_word(content)
    specific_word_count = count_specific_word(content, specific_word) if specific_word else 0
    avg_length = average_word_length(content)
    percentage_longer = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {unique_word_count}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Longest word: '{longest_word}'")
    if specific_word:
        print(f"Occurrences of '{specific_word}': {specific_word_count}")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than average: {percentage_longer:.2f}%")

analyze_text('sample.txt', specific_word='example') 
