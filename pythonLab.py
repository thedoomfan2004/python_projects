import random;
import string;

# b = random.randint(1, 100)

# a = int(input('number: '))



# if a > b:
#     print('меньше !')
# elif a < b:
#     print('больше !')

# a = int(input('number: '))



# if a > b:
#     print('меньше !')
# elif a < b:
#     print('больше !')

# a = int(input('number: '))



# if a > b:
#     print('меньше !')
# elif a < b:
#     print('больше !')

# print('число:', b)


















a = int(input('number: '))
b = ''


res = [int(x) for x in str(a)]


if len(res) == 6:
    if res[0] == int(1):
        b += 'сто '
        res.pop(0)
    elif res[0] == int(2):
        b += 'двести '
        res.pop(0)
    elif res[0] == int(3):
        b += 'триста '
        res.pop(0)
    elif res[0] == int(4):
        b += 'четыреста '
        res.pop(0)
    elif res[0] == int(5):
        b += 'пятсоть '
        res.pop(0)
    elif res[0] == int(6):
        b += 'шестсот '
        res.pop(0)
    elif res[0] == int(7):
        b += 'семьсот '
        res.pop(0)
    elif res[0] == int(8):
        b += 'восемсот '
        res.pop(0)
    elif res[0] == int(9):
        b += 'девятьсот '
        res.pop(0)
    elif res[0] == int(0):
        b += ''
        res.pop(0)


if len(res) == 5:
    if res[0] == int(1):
        b += 'десить '
        res.pop(0)
    elif res[0] == int(2):
        b += 'двадцать '
        res.pop(0)
    elif res[0] == int(3):
        b += 'тридцать '
        res.pop(0)
    elif res[0] == int(4):
        b += 'сорок '
        res.pop(0)
    elif res[0] == int(5):
        b += 'пятдесять '
        res.pop(0)
    elif res[0] == int(6):
        b += 'шестдесят '
        res.pop(0)
    elif res[0] == int(7):
        b += 'семдесять '
        res.pop(0)
    elif res[0] == int(8):
        b += 'восемдесять '
        res.pop(0)
    elif res[0] == int(9):
        b += 'девяноста  '
        res.pop(0)
    elif res[0] == int(0):
        b += ''
        res.pop(0)


if len(res) == 4:
    if res[0] == int(1):
        b += 'тысячи '
        res.pop(0)
    elif res[0] == int(2):
        b += 'две тысячи '
        res.pop(0)
    elif res[0] == int(3):
        b += 'три тысячи '
        res.pop(0)
    elif res[0] == int(4):
        b += 'четыре тысячи '
        res.pop(0)
    elif res[0] == int(5):
        b += 'пять тысячи '
        res.pop(0)
    elif res[0] == int(6):
        b += 'шесть тысячи '
        res.pop(0)
    elif res[0] == int(7):
        b += 'семь тысячи '
        res.pop(0)
    elif res[0] == int(8):
        b += 'восемь тысячи '
        res.pop(0)
    elif res[0] == int(9):
        b += 'девять тысячи '
        res.pop(0)
    elif res[0] == int(0):
        b += ''
        res.pop(0)

if len(res) == 3:
    if res[0] == int(1):
        b += 'сто '
        res.pop(0)
    elif res[0] == int(2):
        b += 'двести '
        res.pop(0)
    elif res[0] == int(3):
        b += 'триста '
        res.pop(0)
    elif res[0] == int(4):
        b += 'четыреста '
        res.pop(0)
    elif res[0] == int(5):
        b += 'пятьсот '
        res.pop(0)
    elif res[0] == int(6):
        b += 'шестьсот '
        res.pop(0)
    elif res[0] == int(7):
        b += 'семьсот '
        res.pop(0)
    elif res[0] == int(8):
        b += 'восемьсот '
        res.pop(0)
    elif res[0] == int(9):
        b += 'девятьсот '
        res.pop(0)
    elif res[0] == int(0):
        b += ''
        res.pop(0)

if len(res) == 2:
    if res[0] == int(1):
        b += 'Десять '
        res.pop(0)
    elif res[0] == int(2):
        b += 'двадцать '
        res.pop(0)
    elif res[0] == int(3):
        b += 'тридцать '
        res.pop(0)
    elif res[0] == int(4):
        b += 'сорок '
        res.pop(0)
    elif res[0] == int(5):
        b += 'пятдесять '
        res.pop(0)
    elif res[0] == int(6):
        b += 'шестдеять '
        res.pop(0)
    elif res[0] == int(7):
        b += 'семдесыать '
        res.pop(0)
    elif res[0] == int(8):
        b += 'восемдесять '
        res.pop(0)
    elif res[0] == int(9):
        b += 'девяноста '
        res.pop(0)
    elif res[0] == int(0):
        b += ''
        res.pop(0)





if len(res) < 2:
    if res[0] == int(1):
        b += 'один'
    elif res[0] == int(2):
        b += 'два'
    elif res[0] == int(3):
        b += 'три'
    elif res[0] == int(4):
        b += 'четыре'
    elif res[0] == int(5):
        b += 'пять'
    elif res[0] == int(6):
        b += 'шесть'
    elif res[0] == int(7):
        b += 'семь'
    elif res[0] == int(8):
        b += 'восемь'
    elif res[0] == int(9):
        b += 'девять'



print(b)












# # # number = int(input('number: '))



# def num_to_word(number):
#     # Define word lists for units, tens, and hundreds
#     units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#     hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    
#     # Split the number into its digits
#     num_list = list(str(number))

#     # Check the number of digits
#     if len(num_list) == 1:
#         # Single-digit numbers
#         return units[int(num_list[0])]
#     elif len(num_list) == 2:
#         # Two-digit numbers
#         if int(num_list[0]) == 1:
#             return " ".join([tens[int(num_list[1])]])
#         else:
#             return " ".join([tens[int(num_list[0])], units[int(num_list[1])]])
#     elif len(num_list) == 3:
#         # Three-digit numbers
#         if int(num_list[1:]) == 0:
#             return " ".join([hundreds[int(num_list[0])]])
#         else:
#             return " ".join([hundreds[int(num_list[0])], "and", num_to_word(int(num_list[1:]))])
#     else:
#         # Unsupported numbers
#         return "unsupported number"








# print(num_to_word(23))





# a = ''

# b = random.randint(6, 20)
# # c = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# # d = 'qwertyuiopasdfghjklzxcvbnm'

# res = [int(x) for x in str(b)]

# while len(res) < 4:
#    res.append(random.randint(1, 9)) 

# res.insert(random.randint(1, len(res)), '-')



# for i in res:
#   print(i, end="")
  

# print(res) 



























a = []


while len(a) < 10:
    b = random.randint(1, 50)
    if b % 2 == 0:
        a.append(b)

print('ss')

