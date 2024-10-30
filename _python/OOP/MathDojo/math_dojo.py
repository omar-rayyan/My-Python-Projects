class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self


md1 = MathDojo()
x1 = md1.add(7).add(2,5,1).subtract(3,2).result
print(x1)

md2 = MathDojo()
x2 = md2.add(1).add(9,20,30,40,5).subtract(3,2).subtract(1).add(5).result
print(x2)

md3 = MathDojo()
x3 = md3.add(10).add(8,5,6).subtract(5,1).result
print(x3)