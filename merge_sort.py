import time
import math

with open("number2.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))


def merge_sort(num_list):
    # 入力の整数列の長さ
    length = len(num_list)

    if len(num_list) > 1:
        left = merge_sort(num_list[: math.ceil(length / 2)])  # 半分より左側
        right = merge_sort(num_list[math.ceil(length / 2) :])  # 半分より右側
        merge = []

        # 左側と右側のどちらかの中身がなくなるまで、小さいものをmergeに入れていく
        while len(right) != 0 and len(left) != 0:
            if right[0] < left[0]:
                merge.append(right.pop(0))
            else:
                merge.append(left.pop(0))
        # どちらかがなくなったら、もう片方を全部mergeに入れる
        if len(right) != 0:
            merge.extend(right)
        if len(left) != 0:
            merge.extend(left)
        return merge
    else:
        return num_list


start = time.time()
ans = merge_sort(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])