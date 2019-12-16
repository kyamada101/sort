#再帰を使わないヒープソート
import time
import math

with open("number3.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))

def heap_sort2(num_list):
    #答えを入れるリスト
    ans = []
    
    while(len(num_list) > 0):
        length = len(num_list)

        #入力されたリストをヒープ木とみなしてソートする
        for i in range(((length // 2) - 1), -1, -1):

            #小さければ親ノードと交換(子ノードのインデックスが小さい方)
            if (num_list[2 * i + 1] < num_list[i]):
                num_list[2 * i + 1], num_list[i] = num_list[i], num_list[2 * i + 1]

            #一番枝葉の子ノードが1つしかなかった場合はここでcontinue
            if (length % 2 == 0) and (i == (length // 2) - 1):
                continue

            #小さければ親ノードと交換(子ノードのインデックスが大きい方)
            if (num_list[2 * i + 2] < num_list[i]):
                num_list[2 * i + 2], num_list[i] = num_list[i], num_list[2 * i + 2]

            #ここまでで根(一番親のノード=num_list[0])に最大値が来るはず

        ans.append(num_list.pop(0))
    
    return ans

start = time.time()
ans = heap_sort2(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])