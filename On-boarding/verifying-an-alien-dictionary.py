class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict={alpha:indx for indx,alpha in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j==len(words[i+1]):
                    return False
                if words[i][j]!=words[i+1][j]:
                    if order_dict[words[i][j]]>order_dict[words[i+1][j]]:
                        return False
                    break
        return True