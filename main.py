print("hello world")


path_to_file = "books/frankenstein.txt"

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_count = dict()
    for character in text:
        if character not in character_count.keys():
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count


if __name__ == "__main__":
    with open(path_to_file) as f:
        file_contents = f.read()
print(f"--- Begin report of {path_to_file} ---")
print(f"{count_words(file_contents)} words found in the document")
for key, item in count_characters(file_contents).items():
    print(f"The '{key}' character was found {item} times")
print(f"--- End report ---")