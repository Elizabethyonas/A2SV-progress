class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penality = float('inf')
        hour = 0
        count_N = 0
        count_Y = 0
        i = 0
        for chr in customers:
            if chr == "Y":
                count_Y +=1
            
        while i < len(customers):
            curr = count_Y + count_N
            if curr < penality:
                penality = curr
                hour = i
            if customers[i] == "Y":
                count_Y -= 1
            else:
                count_N += 1
            i += 1
        curr = count_Y + count_N
        if curr < penality:
            penality = curr
            hour = i
        return hour
        