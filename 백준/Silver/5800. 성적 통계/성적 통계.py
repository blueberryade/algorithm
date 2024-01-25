k = int(input())
for i in range(1,k+1):
    nums = list(map(int,input().split()))
    nums = nums[1:]
    nums.sort()
    max_num = max(nums)
    min_num = min(nums)
    diff = []
    for j in range(len(nums)-1):
        diff.append(nums[j+1]-nums[j])
    print('Class', i)
    print('Max %d, Min %d, Largest gap %d'%(max_num,min_num,max(diff)))