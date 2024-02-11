class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        check=defaultdict(int)
        max_fruit=0
        j=0
        for i in range(len(fruits)):
            check[fruits[i]]+=1
            while len(check)>2:
                check[fruits[j]]-=1
                
                if not check[fruits[j]]:
                    check.pop(fruits[j])
                j+=1
            max_fruit=max(max_fruit,i-j+1)
                
            
            
        return max_fruit


