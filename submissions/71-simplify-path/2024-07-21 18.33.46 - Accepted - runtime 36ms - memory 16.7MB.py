class Solution:
    def simplifyPath(self, path: str) -> str:
        #must start with /
        #should not end with /
        
        stack = []
        
        for i in path.split("/"):
            if i =="..":
                if stack:
                    stack.pop()
            elif i =="." or not i:
                continue
                
            else:
                stack.append(i)
                
        return "/"+ "/".join(stack)