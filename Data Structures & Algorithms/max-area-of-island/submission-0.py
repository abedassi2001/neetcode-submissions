class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxl = 0 
        visit = set()
        if not grid : 
            return 0

        row , col = len(grid) , len(grid[0])
        def dfs(row , col ):
            length = 1
            q = deque()
            q.append((row,col))
            while q :
                r , c = q.pop()
                dirc = [[1,0],[0,1],[-1,0],[0,-1]]
                for rdir , cdir in dirc :
                    cd , rd = cdir + c , rdir + r
                    if (rd in range(len(grid)) and cd in range(len(grid[0]))
                    and grid[rd][cd] == 1 and (rd,cd) not in visit):
                        length += 1
                        visit.add((rd,cd))
                        q.append((rd,cd))
            return length                    

        for i in range(row):
            for j in range(col):
                if ((i , j) not in visit
                and grid[i][j] == 1):
                    visit.add((i,j))
                    maxl = max(maxl,dfs(i,j))
        return maxl                


        