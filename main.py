def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    h = count_characters(text)
    print_report(text,h)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    # Alle Zeichen in Kleinbuchstaben umwandeln
    text = text.lower()

    # Ein leeres Dictionary zum Speichern der Häufigkeit jedes Zeichens erstellen
    frequency = {}

    # Durch jeden Buchstaben in der Zeichenfolge iterieren
    for char in text:
        # Nur Buchstaben zählen, keine Sonderzeichen oder Leerzeichen
        if char.isalpha():
            # Buchstaben zur Häufigkeit hinzufügen oder die Zählung erhöhen
            frequency[char] = frequency.get(char, 0) + 1

    return frequency

def print_report(text, frequency):
    num_words = len(text.split())
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    for char, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{char}' character was found {freq} times")
        
    print("--- End report ---")


main()