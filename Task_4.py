## 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = 'AAABBBBCCCCC'               # input("Input Your text here: ")
str_to_list = []
encoding = []
decoding = []
count = 1

for i in text:
    str_to_list.append(i)

str_to_list.append('9')                                 # adding any item for length


for i in range(len(str_to_list)- 1):                    # encoding
    if str_to_list[i] == str_to_list[i + 1]:
        count += 1
    else:
        if count > 1:
            encoding.append(count)
            encoding.append(str_to_list[i])
        else:
            encoding.append(str_to_list[i])
        count = 1

print(*encoding)
                                                        
def qnt_append(int, char, list):                        # decoding
    while int > 1:
        list.append(char)
        int -= 1


for i in range(len(encoding)):
    if type(encoding[i]) == int:
        qnt_append(encoding[i], encoding[i + 1], decoding)
    else:
        decoding.append(encoding[i])

print(decoding)