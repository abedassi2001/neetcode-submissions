class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid : 
            return 0
        visit = set()            
        islands = 0            
        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                print(grid[i][j])
                print(visit)
                if grid[i][j] == "1" and (i,j) not in visit :
                    print( " it got here")
                    islands += 1 
                    visit.add((i,j))
                    self.dfs( grid, visit, i, j)
        return islands                    




    def dfs(self , grid, visit, i, j ) :
        q = deque()
        q.append((i,j))
        while q :
            row , col  = q.pop()
            dir_dfs = [[1,0] , [0,1] ,[-1,0],[0,-1]]
            for rdir , cdir in dir_dfs :
                c , r = col + cdir , row + rdir
                if (r in range(len(grid)) and c in range (len(grid[0]))  
                and (grid[r][c] == "1") and (r,c) not in visit):
                     q.append((r,c))
                     visit.add((r,c))                 



                        


        