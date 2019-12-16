import time
import math

with open("number1.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))


def choice_sort(num_list):
    for i in range(1, len(num_list) - 2):

        # 最小値のインデックス番号を取得
        min_value = num_list[i + 1]
        for k in range(i, len(num_list) - 1):
            if num_list[k] < min_value:
                min_value = num_list[k]
                index = k

        # それとi-1番目の要素を交換
        if num_list[index] < num_list[i - 1]:
            num_list[index], num_list[i - 1] = num_list[i - 1], num_list[index]
    return num_list


start = time.time()
ans = choice_sort(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])