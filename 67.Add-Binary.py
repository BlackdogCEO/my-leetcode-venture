class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a.__len__() < b.__len__():
            c = a
            a = b
            b = c
        i = 1
        j = 1
        carry = 0
        c = []
        while i <= len(a):
            if i <= len(b):
                c.append((int(a[-i]) + int(b[-i]) + carry) % 2)
                carry = (int(a[-i]) + int(b[-i]) + carry) // 2
            else:
                c.append((int(a[-i]) + carry) % 2)
                carry = (int(a[-i]) + carry) // 2
            i += 1
        if carry == 1:
            c.append(1)
        c.reverse()

        return "".join([str(i) for i in c])

"""

Runtime: 52 ms, faster than 47.43% of Python3 online submissions for Add Binary.
this version is already nearly best.
some simply use built in model like bin,eval...


"""