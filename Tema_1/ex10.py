def count_words(text):
    words = text.split(" ")
    return len(words)

text = input("Introduceți un text: ")
result = count_words(text)

print(f"Numărul de cuvinte din text este: {result}")
