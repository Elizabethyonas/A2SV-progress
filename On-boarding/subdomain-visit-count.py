class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        HashMap = defaultdict(int)
        
        for domain in cpdomains:
            c, dom = domain.split()
            
            dom = dom.split('.')
            for i in range(len(dom)):
                HashMap[tuple(dom[i:])] += int(c)
        
        ans = []
        for dom, c in HashMap.items():
            ans.append(str(c) + ' ' + '.'.join(dom))
        
        return ans
