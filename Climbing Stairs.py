# Time Complexity - O(2^N)
# Space complexity - O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        
        return self.backtrack(n,0,0,[])

    def backtrack(self,n,steps,count,res):

        if steps == n:
            res.extend([steps])
            # print(res)
            count += 1
            return len(res)
            
        if steps > n:
            return 0


        for i in range(1,3):

            count = self.backtrack(n,steps+i,count,res)
            # steps = steps-i

        return len(res)


# Time Complexity - O(N)
# Space complexity - O(1)

class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        first_jump = 1
        second_jump = 2
        final_jump = 0

        for i in range(2,n):
            final_jump = first_jump + second_jump
            first_jump = second_jump
            second_jump = final_jump

        return final_jump