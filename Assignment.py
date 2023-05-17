def findNumbers(array,targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while left < right:
        currentSum = array[left]+array[right]
        if currentSum == targetSum:
            
            print(left,right)
            return left+right
        elif currentSum < targetSum:
            left+=1
        elif currentSum >  targetSum:
            right-=1


nums = [2.5,7.5,11.2,15.1]
target = 11.2 + 15.1

print(findNumbers(nums,target))