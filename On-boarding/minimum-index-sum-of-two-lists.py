class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        answer=[]
        minimum=float('inf')
        for i,val1 in enumerate(list1):
            for j,val2 in enumerate(list2):
                if val1==val2:
                    mini=i+j
                    if mini==minimum:
                        minimum=mini
                        answer.append(val1)
                    elif mini<minimum:
                        minimum=mini
                        answer.clear()
                        answer.append(val1)
        return answer
        
