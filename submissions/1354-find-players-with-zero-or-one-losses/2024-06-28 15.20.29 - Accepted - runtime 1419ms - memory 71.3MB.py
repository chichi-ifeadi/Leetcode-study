class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        lst1=[]
        lst2=[]
        for match in matches:
                count[match[0]]+=0
                count[match[1]]+=1
        
        
        print(count)
        for key,value in count.items():
            if value ==0:
                lst1.append(key)
            elif value ==1:
                lst2.append(key)
        return [sorted(lst1),sorted(lst2)]
                