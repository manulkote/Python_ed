words = ['разработка', 'администрирование', 'protocol', 'standard']
words_b = []
for i in words:
    words_b.append(i.encode('utf-8'))
print(words_b)
words = []
for i in words_b:
    words.append(i.decode('utf-8'))
print(words)
