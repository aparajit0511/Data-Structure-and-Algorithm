# Time Complexity: O(N) and Space Complexity: O(1)
import re
class Solution:
    def isPalindrome(self, mystring: str) -> bool:
        mystring = re.sub('[^A-Za-z0-9]+', '', mystring).lower()
        mystring = list(mystring)
        print(mystring)

        left , right = 0 , len(mystring)-1

        while left <= right:
        	if mystring[left] != mystring[right]:
        		return False
        	left +=1
        	right -= 1

        return True