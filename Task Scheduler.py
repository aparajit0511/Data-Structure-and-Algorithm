# Time Complexity - O(N)
# Space complexity - O(N)

from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = defaultdict(int)
        frequency = 0
        max_tasks = 0
        total_tasks = len(tasks)

        # count max frequency in the list of tasks
        for task in tasks:
            task_count[task] += 1

            if frequency < task_count[task]:
                frequency = task_count[task]


        # check number of tasks having maximum frequency
        for count in task_count.values():
            if count == frequency:
                max_tasks += 1

        # use formula - max ( (n+1)*(f-1) + X, TotalJobs)

        return max((frequency-1) * (n+1) + max_tasks,total_tasks)