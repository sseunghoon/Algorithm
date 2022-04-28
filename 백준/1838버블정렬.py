import sys
input = sys.stdin.readline
from collections import defaultdict

max_difference = 0

N = int(input())
arr = list(map(int,input().split()))
sorted_arr = sorted(arr)

idx_dict = defaultdict(int)

for i in range(N-1,-1,-1):
    idx_dict[sorted_arr[i]] = i

max_difference_num = arr[0]
for i in range(N):
    difference = abs(i - idx_dict[arr[i]])
    if max_difference < difference:
        if i == 0:
            max_difference = difference
        elif max_difference_num == arr[0]:
            max_difference = min(max_difference,difference)
        else:
            max_difference = difference

print(sorted_arr)
print(max_difference)

# 7
# 27 10 10 44 49 50 60 27
# dict에 num마다의 가장 작은 인덱스, 가장 큰 인덱스를 넣어야 하나 고민 중
