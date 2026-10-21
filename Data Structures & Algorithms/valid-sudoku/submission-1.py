from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in board:
            seen = defaultdict(int)
            for ele in col:
                seen[ele] += 1
                if seen[ele] >= 2 and ele != ".":
                    return False
        for i in range(len(board[0])):
            seen = defaultdict(int)
            for j in range(len(board)):
                ele = board[j][i]
                seen[ele] += 1
                if seen[ele] >= 2 and ele != ".":
                    return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                seen = defaultdict(int)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        ele = board[k][l]
                        seen[ele] += 1
                        if seen[ele] >= 2 and ele != ".":
                            return False
    


        return True
            

        