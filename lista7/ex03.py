# conta quantas vezes aparece o 9 numa lista nums
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

print(array_count9([9,10,9,10,9,10]))