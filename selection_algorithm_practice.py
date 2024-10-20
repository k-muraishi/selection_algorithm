import random

def selection_algorithm(numbers):
    length = len(numbers)

    # 単純な選択アルゴリズム
    for i in range(length):
        for j in range(i + 1, length): # iの右隣と比較する
            if numbers[j] < numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp # 値を入れ替える

    # 0が先頭に来ないようにする
    if numbers[0] == 0:
        for k in range(1, length):
            if numbers[k] != 0:
                numbers[0] = numbers[k]
                numbers[k] = 0
                break

    return numbers

# numbers = [7, 4, 3, 8, 1, 5, 2, 6, 0, 0, 0]
numbers = [random.randint(0, 9) for _ in range(9)]
result = selection_algorithm(numbers)
print(result)
