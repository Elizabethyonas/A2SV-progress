class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances={}
        check=defaultdict(int)
        ans=[]
        for x,y in points:
            distances[(x,y)]=(x*x + y*y)**0.5
            check[(x,y)]+=1
        for key,value in sorted(distances.items(), key=lambda x: x[1]):
            for i in range(check[key]):
                ans.append(list(key))
                k-=1
            if k==0:
                break
        return ans
