print("Введите размер коврика (нечетное число): ")
i_sizeheig = int(input())
i_widt = i_sizeheig * 3

for i_count in range(1, i_sizeheig, 2):
    print(('X|X' * i_count).center(i_widt, '*'))

print('WELCOME'.center(i_widt, '?'))

for count in range(i_sizeheig-2, 0, -2):
    print(('X|X' * i_count).center(i_widt, '*'))