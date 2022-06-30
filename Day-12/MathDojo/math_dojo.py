class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        if(nums):
            for i in nums:
                self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        if(nums):
            for i in nums:
                self.result -= i
        return self


md = MathDojo()
x = md.add(10).add(3).subtract(2,1,3).result
print(x)	# should print 7

