from collections import Counter

def word_count_and_top_words(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()

    words = text.split()

    word_counts = Counter(words)

    top_words = word_counts.most_common(5)

    print(f"Total words (case-sensitive): {len(words)}")

    print("\nTop 5 words:")
    for word, count in top_words:
        print(f"{word}: {count}")

file_path = 'Lloyd Alexander - [Chronicles Of Prydain 3] Castle Of Llyr.txt'
word_count_and_top_words(file_path)
