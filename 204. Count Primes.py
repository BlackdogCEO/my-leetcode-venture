class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 2 >= n:
            return 0
        lis = [True] * (n - 2)
        i = 2
        while i ** 2 < n:
            if not lis[i - 2]:
                i += 1
            else:
                j = i ** 2
                while j < n:
                    lis[j - 2] = False
                    j += i
                i += 1
        cont = 0
        for i in lis:
            if i:
                cont += 1
        return cont

"""
Runtime: 508 ms, faster than 55.96% of Python online submissions for Count Primes.
using Sieve of Eratosthenes. The idea is to label multiples of numbers, in the same time, no need to consider the numbers
which has already benn labeled, so for 2, we know 2*2,2*3....is not prime, then for 3,,, for 4,because it is already labeled
,so skip it ...,
some little skills like we only need to consider until n**0.5 because any number greater than that, if it is not a prime,
which equals p*q, will have a factor which is less than n**0.5
another skill is that for a certain number in consideration, like 3, we only nedd to start label from 3*3,because anything less
than that, like 3*2, is already labeled in consideration for 2.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 2 >= n:
            return 0
        lis = [True] * n
        lis[0:2] = [False] * 2
        for i in range(2, int(n ** 0.5) + 1):
            if lis[i]:
                lis[i * i:n:i] = [False] * len(lis[i * i:n:i])
        return sum(lis)


"this is other's version using slice in python, which is much simple and elegant"