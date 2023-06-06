from django.test import TestCase


#def counter(func):
    #COUNTER = 0
    #def wrapper():
        #print('Before')
        #nonlocal COUNTER
        #COUNTER +=1
        #print(COUNTER)
       # result = func()
        #print(f"Resolt:{result}")
        #print('After')
    #return wrapper

#@counter
#def foo():
    #return "None"

#foo = counter(foo)
#foo()
#foo()
#foo()

class Solution(object):
    def twoSum(self, nums, target):
        self.nums = list(nums)
        self.target = int(target)

        nums2 = []
        for i in nums:
            nums2.append(i)
        chislo = 0
        shechik = 0
        while shechik != target:
            for num in nums2:
                chislo += num
                if chislo > target:
                    raznica = chislo - target
                    nums2.remove(raznica)
                    chislo = 0
            konec_cikla = sum(nums2)
            shechik = konec_cikla
        final = []
        varik = 0
        bukva =0
        for i in nums2:
            if nums[bukva] != i:
                bukva += 1
                varik += 1
            if i in nums:
                plusik = nums.index(i,varik)
                final.append(plusik)
                varik += 1
                continue
            if varik not in nums2:
                break
        return(final)


num = [2,7,11,15]
targ = 9
test = Solution()
print(test.twoSum(num,targ))
