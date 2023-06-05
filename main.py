from time import perf_counter
from trie import trieDS

def main():
    
    print("Initializing data-structure")
    init_start_time = perf_counter()
    trie = trieDS()
    with open("words_alpha.txt", "r") as f:
        lines = f.readlines()

    for word in lines:
        trie.add_word(word.strip())
    word_count = len(lines)
    del lines
    init_fin_time = perf_counter()

    print(f"Initialization ready. Took {init_fin_time - init_start_time} seconds")
    print(f"Added {word_count} words.")

    while True:
        word_to_check = input("Check if word exists: ")
        res = trie.find_word(word_to_check)
        if res:
            print(f"{word_to_check} is a word!\n")
        else:
            print(f"{word_to_check} is not a word\n")

if __name__ == "__main__":
    main()