import re

# Split a paragraph into sentences using regex
def split_sentences(paragraph):
    # Regex matches sentences ending with . ? or !
    pattern = r'[^.!?]+[.!?]'
    return re.findall(pattern, paragraph)


# Display each sentence and the total count
def display_sentences(sentences):
    for idx, sentence in enumerate(sentences, start=1):
        print(f"Sentence {idx}: {sentence.strip()}")
    print(f"\nTotal Sentences: {len(sentences)}")


# Main function: get input and run processing
def main():
    print("=== Sentence Splitter Program ===")
    paragraph = input("Enter a paragraph: ")

    sentences = split_sentences(paragraph)
    display_sentences(sentences)


# Run program
if __name__ == "__main__":
    main()
