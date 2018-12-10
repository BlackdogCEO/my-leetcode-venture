class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        ans="1"
        i=1
        while i<n:
            j=0
            k=1  #k indicate how much same number showed up continuously
            ans1="" #the next generated string based on the former string
            while j<len(ans)-1:
                if ans[j]==ans[j+1]:
                    k+=1
                    j+=1
                else:
                    ans1+=str(k)
                    ans1+=ans[j]
                    k=1
                    j+=1
            ans1+=str(k)
            ans1+=ans[j]
            ans=ans1
            i+=1
        return ans

"""
Runtime: 40 ms, faster than 87.76% of Python3 online submissions for Count and Say.
just use 2 cycles to accomplish it.
we start from the n=1, then 2,3...
for certain string, we count it to say the next string,and continue to the required
answer, n=i relies on n=i-1, ......
still, whether the index is out of range is an annoying question
"""