# 1. Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке.
# Выведите оба количества на экран. (использовать цикл)

try:
    text = input("Enter text: ")
    numbers = 0
    letters = 0
    for i in text:
        if i.isalpha():
            letters += 1
        if i.isdigit():
            numbers += 1
    print("Num of letters:", letters)
    print("Num of numbers:", numbers)
except Exception as error:
    print(error)

# 2. Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке
# встречается искомый символ. Полученное число выведите на экран.

try:
    text = input("Enter text: ")
    symbol = input ("Enter symbol to search: ")
    sum_symbols = 0
    for i in text:
        if i == symbol:
            sum_symbols += 1
    print("Num of searching symbols:", sum_symbols)
except Exception as e:
    print(e)

# 3. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в
# строке замену одного слова на другое. Полученную строку отобразите на экране.

text = input("Enter text: ")
text_for_search = input ("Enter word for search: ")
text_for_replacement = input("Enter word for replacement: ")
text = text.replace(text_for_search, text_for_replacement)
print(text)

# 4. Дана строка. (сделать срезы)
#
# - Сначала выведите третий символ этой строки.
# - Во второй строке выведите предпоследний символ этой строки.
# - В третьей строке выведите первые пять символов этой строки.
# - В четвертой строке выведите всю строку, кроме последних двух символов.
# - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# - В седьмой строке выведите все символы в обратном порядке.
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# - В девятой строке выведите длину данной строки.

text = input("Enter text: ")
print("Third character of a string:", "\n\t",  text[2])
print("Penultimate character of a string:", "\n\t", text[-2])
print("First five characters of a string:", "\n\t",  text[:5])
print("The entire string except the last two characters:", "\n\t",  text[:-2])
print("All characters with even indices:", "\n\t",  text[::2])
print("All characters with odd indices:", "\n\t",  text[1::2])
print("All characters in reverse order:", "\n\t",  text[::-1])
print("All characters of the string in reverse order. Through one:", "\n\t",  text[-1::-2])
print("Line length:", "\n\t",  len(text))

# Дополнительно:
#
# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в тексте.
