import time
import math
import sys

sys.setrecursionlimit(100000)

with open("number3.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))

def heap_sort(num_list):
    length = len(num_list)
    
    #長さが1になったらそのまま返す
    if length == 1:
        return num_list
    
    #入力されたリストをヒープ木とみなしてソートする
    for i in range(((length // 2) - 1), -1, -1):

        #大きければ親ノードと交換(子ノードのインデックスが小さい方)
        if (num_list[2 * i + 1] > num_list[i]):
            num_list[2 * i + 1], num_list[i] = num_list[i], num_list[2 * i + 1]

        #一番枝葉の子ノードが1つしかなかった場合はここでcontinue
        if (length % 2 == 0) and (i == (length // 2) - 1):
            continue

        #大きければ親ノードと交換(子ノードのインデックスが大きい方)
        if (num_list[2 * i + 2] > num_list[i]):
            num_list[2 * i + 2], num_list[i] = num_list[i], num_list[2 * i + 2]

        #ここまでで根(一番親のノード=num_list[0])に最大値が来るはず

    #最大値を一番後ろに持ってくる
    num_list[0], num_list[-1] = num_list[-1], num_list[0]
    
    #一番後ろより一個手前までで再帰的にヒープソート
    return heap_sort(num_list[:-1]) + [num_list[-1]]

start = time.time()
ans = heap_sort(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])