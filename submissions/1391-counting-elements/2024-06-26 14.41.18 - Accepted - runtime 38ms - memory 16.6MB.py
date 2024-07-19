class Solution:
    def countElements(self, arr: List[int]) -> int:
        #check if num+ 1 is in the array
        #need to account for duplicatiates
        
        #take num check if num +1 is in array
        #if it is add that num to my set 
        '''
        if i find
        i could use a dict
        add their frequecies
        if num is in the dict decremnet the value
        if less than 1 then we know that we have reached the limit'''
        
        count = 0
        
        '''my_dict = {}
        
        for i in arr:
            my_dict[i]=my_dict.get(i, 0)+1
        
        
        print(my_dict)
        
        for key in my_dict:
          
                if key+1 in my_dict:
                    
                    count+=my_dict[key]
              
        return count'''
        seen = set(arr)
        
        for i in arr:
            if i+1 in seen:
                count+=1
        return count
            
                
        