class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        counter = 0 
        timer = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 :
                    queue.append((i,j))
                if grid[i][j] == 1 :
                    counter += 1                     

        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        while len(queue) and counter > 0 :
            
            length = len(queue)
            
            for i in range(length):
                idx = queue.popleft()

                for dc , dr in dir :

                    nc = dc + idx[0]
                    nr = dr + idx[1]
                
                    if  nc >= 0 and nc < len(grid) and nr >= 0 and nr < len(grid[0]) and grid[nc][nr] == 1 :
                        queue.append((nc,nr))
                        grid[nc][nr] = 2 
                        counter -= 1 

            timer += 1

        if counter > 0 :
            return -1
        return timer                                

                        
