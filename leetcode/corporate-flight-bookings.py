class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer=[0]*(n+1)
        for i in range(len(bookings)):
            l=bookings[i][0]
            r=bookings[i][1]
            seats=bookings[i][2]
            answer[l-1]+=seats
            answer[r]-=seats
             
        for j in range(1,n):
            answer[j]+=answer[j-1]
            

        return answer[:n]
