import time
import math

with open("number2.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))


def quick_sort(num_list):
    # 配列に1個しか数字が入ってなければそのまま返す
    if len(num_list) == 1:
        return num_list

    # 基準になる数
    criterion = num_list[0]  # 配列の一番先頭を基準にする

    # 動かす軸
    Lindex = 0
    Rindex = len(num_list) - 1

    while True:
        # 左から基準以上の数を探す
        while num_list[Lindex] < criterion:
            Lindex += 1
            # 一番右端までいったらbreak
            if Lindex == len(num_list):
                break
        # 右から基準より小さい数を探す
        while num_list[Rindex] >= criterion:
            Rindex -= 1
            # 一番左端まで行ったらbreak
            if Rindex == -1:
                break

        if Lindex >= Rindex:
            break

        # 見つけたものをまず入れ替える
        num_list[Lindex], num_list[Rindex] = num_list[Rindex], num_list[Lindex]

    # 配列に基準の数以上のものしかなかった場合は、左右の切る場所を変える
    if Lindex == 0 and Rindex == -1:
        left = num_list[: Lindex + 1]
        right = num_list[Lindex + 1 :]
    else:
        left = num_list[:Lindex]
        right = num_list[Lindex:]

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    return quick_sort(left) + quick_sort(right)


start = time.time()
ans = quick_sort(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])