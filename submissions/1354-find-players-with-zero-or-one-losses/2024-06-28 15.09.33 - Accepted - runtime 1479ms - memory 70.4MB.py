class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        lst1=[]
        lst2=[]
        for match in matches:
            for i in range(0,len(match)-1):
                count[match[i]]+=0
                count[match[i+1]]+=1
        
        
        print(count)
        for key,value in count.items():
            if value ==0:
                lst1.append(key)
            elif value ==1:
                lst2.append(key)
        return [sorted(lst1),sorted(lst2)]
                