import time

with open("number2.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))


def bucket_sort(num_list):
    # 入力の整数リストに対して、一番大きい要素を取得
    max_int = max(num_list)
    # 0～最大値までバケットを用意
    bucket = [0] * (max_int)

    # 入力の整数列に対して、バケットに値を入れていく（ここでは、その整数のインデックス番号のバケットの値を1増やす）
    for i in range(len(num_list)):
        bucket[num_list[i] - 1] += 1

    ans_list = []
    # バケットの数字＝そのインデックス番号の数字が何個あるか、なので、ansにその個数分入れていく
    for i in range(len(bucket)):
        for k in range(bucket[i]):
            ans_list.append(i + 1)
    return ans_list


start = time.time()
ans = bucket_sort(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])