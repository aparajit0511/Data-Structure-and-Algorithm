# There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        count_tile = 0
        
        for i in range(len(colors)):
            left = (i-1) % len(colors)
            right = (i+1) % len(colors)
            
            if colors[i] != colors[left] and colors[i] != colors[right]:
                count_tile += 1
            
        return count_tile
            
        