class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.min = [float("inf")]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        if self.min[-1] >= x:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.q:
            if self.q[-1] == self.min[-1]:
                self.min.pop()
            self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Runtime: 56 ms, faster than 99.04% of Python3 online submissions for Min Stack.
using 2 stacks and basic list structure to complete this task
there is also another way using only one stack, save the gap between input and min, update min if
input is smaller than min, so a negative saved value means change in min value and can thus be used to
update min val when it is popping, but the question is that there is over flow problem of this solution
if first we got big positive numbers and the very negative numbers
"""