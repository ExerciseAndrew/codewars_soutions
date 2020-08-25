### Not finished witht his code. I'm trying to implement the Kadane algorithm to find the sum of the maximum contiguous subarray
### I'm also trying to do a commit every other day... I have been working on this for a couple of days. I need to commit something.
###
### Visually, I have not come up with much but I have learned a lot and will keep learning.

def max_sequence(arr):
    current_max = [0]
    max_for_now = [0]
    if arr == []:
        return 0
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        max_for_now = max(max_for_now, current_max)
    return max_for_now
