# nums=[7,8,9,0]
#
# it=iter(nums)
#
# print(it.__next__())
# print(it.__next__())
# print(next(it))

class top:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration



value=top()

print(next(value))

for i in value:
    print(i)