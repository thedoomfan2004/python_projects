# import random;

# a = []

# while len(a) < 30:
#     a.append(random.randint(-50, 50))
# max = max(a)
# min = min(a)
# t = 'no'
# lessThanTen = []
# negative = []
# reversed = a[::-1]
# popLastTwenty = a
# replaceItems = []
# p = 0
# zeros = []
# zerosCount = []
# negativesToStr = []
starPositives = []
starNegatives = []
# while p <= 20:
#     p += 1
#     popLastTwenty.pop()

# popTwo = popLastTwenty + popLastTwenty
# a = reversed[::-1]
for i in a:
#     zeros.append(str(i))
    if i >= 0:
        starPositives.append(i)
    if i < 0:
        # negative.append(i)
        starNegatives.append('*')
#     if i >= 0 and i <= 10:
#         lessThanTen.append(i)
#     if i == 13:
#         t = 'yes'

# for o in zeros:
#     for q in o:
#         if q == '0':
#             zerosCount.append(q)
            


# print(a)
# print('max is:', max,'index:' , a.index(max))   
# print('min is:',  min, 'index:', a.index(min))
# print('has thirteen:', t)
# print('amount of zeros:' ,len(zerosCount))
# print('positives lesser than 10:', len(lessThanTen))
# print('amount of negative numbers:', len(negative))
print('negatives to *:', starNegatives + starPositives)
# print('reversed:', reversed)
# print('pop:', popLastTwenty)
# print('pop and duplicate:', popTwo)








