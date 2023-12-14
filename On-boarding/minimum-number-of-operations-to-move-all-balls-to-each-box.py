class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[]
        moves=0
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[i]=='0' and boxes[j]=='1':
                    moves+=abs(i-j)
                elif boxes[i]=='1' and boxes[j]=='1':
                    moves+=abs(i-j)
            answer.append(moves)
            moves=0
        return answer
             
