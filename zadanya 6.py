i_mul = 1
print("Введите число: ")
str_default_number = input()
for i_count in range (0, len(str_default_number)):
    if (str_default_number[i_count] != '0'):
        i_mul *= int(str_default_number[i_count])
print(i_mul)
