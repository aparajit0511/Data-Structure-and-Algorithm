# Most stupidest soluiton ever written

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        import copy

        return copy.deepcopy(node)