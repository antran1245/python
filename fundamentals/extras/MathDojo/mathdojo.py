class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result += num
        for x in nums:
            self.result += x
        return self
    
    def subtract(self, num, *nums):
        # your code here
        self.result -= num
        for x in nums:
            self.result -= x
        return self
    
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

# add tests
add = MathDojo()
result = add.add(2,3).add(5).add(1,2,3,5).result
print(result)

# subtract test
subtract = MathDojo()
result = subtract.subtract(4,2).subtract(3).subtract(5).result
print(result)