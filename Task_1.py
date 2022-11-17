# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = "авб абв ловы лодыв лдфлдвж sабвs абв абв"
output_str = ""

for i in str.split():
    if i.find("абв") == -1:
        output_str += i + ", "
print(output_str)
        