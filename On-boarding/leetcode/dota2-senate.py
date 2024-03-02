class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            radiant_index = radiant.popleft()
            dire_index = dire.popleft()
            
            if radiant_index < dire_index:
                radiant.append(radiant_index + n)
            else:
                dire.append(dire_index + n)

        return "Radiant" if radiant else "Dire"