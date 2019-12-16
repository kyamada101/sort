import time

with open("number2.txt", "r") as f:
    nums = f.read()
    num_list = nums.split(",")
    del num_list[-1]
    num_list = list(map(int, num_list))


def bubble_sort(num_list):
    for i in range(len(num_list) - 1):
        # 先頭から最後のi個手前までforを回す
        for k in range(len(num_list) - 1 - i):
            if num_list[k] > num_list[k + 1]:
                num_list[k], num_list[k + 1] = num_list[k + 1], num_list[k]
    return num_list


start = time.time()
ans = bubble_sort(num_list)
end = time.time()

print("time is {:.3f}secs".format(end - start))
print(ans[0:100])