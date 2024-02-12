class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        
        if N < 2:
            return False
        
        slow = 0 
        
        # fast pointer takes two steps
        fast = nums[0] % N 
        fast = (fast + nums[fast]) % N 
        count = 0
        
        while count < N:
            
            # print(count, nums[slow], nums[fast])
            count += 1
            
            if slow == fast:
                # cycle detected, check length, validate direction
                l = 0 
                step = nums[slow]
                ptr = (nums[slow] + slow) % N # take a step  
                
                while ptr != slow:
                    
                    # check if diff direction 
                    if nums[ptr] * step < 0:
                        break
                    
                    ptr = (ptr + nums[ptr]) % N
                    l += 1
                    
                if l > 0 and ptr == slow:
                    return True 
                
                else: # Must be careful about this update to get out of bad cycles
                    
                    # choose a different starting position (1 jump away from current slow pointer)
                    # consider the fast pointer as also starting from this position, but update it twice 
                    slow = (slow + 1) % N 
                    fast = (slow + nums[slow]) % N 
                    fast = (fast + nums[fast]) % N  
              
            else:
                slow = (slow + nums[slow]) % N 
                fast = (fast + nums[fast]) % N 
                fast = (fast + nums[fast]) % N 
            
        return False