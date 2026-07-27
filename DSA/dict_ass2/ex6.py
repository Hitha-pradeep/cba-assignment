def word_frequency(text):
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    for word, count in frequency.items():
        print(f"{word} -> {count}")


def main():
    text = input("Enter a paragraph: ")
    word_frequency(text)


if __name__ == "__main__":
    main()
