class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        blocks = {}

        for i in range(len(board)):
            for j in range(len(board[0])):

                number = board[i][j]
                block_pos = (i // 3, j // 3)

                if number == ".":
                    continue


                else :

                    if i not in rows :
                        rows[i] = set()

                    if j not in cols :
                        cols[j] = set()

                    if block_pos not in blocks :
                        blocks[block_pos] = set()

                    if number in rows[i] or number in cols[j] or number in blocks[block_pos]:
                        return False

                    rows[i].add(number)
                    cols[j].add(number)
                    blocks[block_pos].add(number)

        return True                                                                 




