from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float("inf")

    def avg(self, nums, lt=None, ut=None):
        if lt is not None:
            nums = [i for i in nums if i >= lt]
        if ut is not None:
            nums = [i for i in nums if i <= ut]
        if nums:
            return sum(nums) / len(nums)
        else:
            return 0
