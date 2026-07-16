class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_sets = {
            'row_sets': [],
            'col_sets': [],
            'square_sets': []    
        }
        
        for _ in range(9):
            board_sets['row_sets'].append(set())
            board_sets['col_sets'].append(set())
            board_sets['square_sets'].append(set())

        for i in range(len(board)):
            for j in range(len(board[i])):
                element = board[i][j]
                if element == ".": continue

                square = (i // 3) * 3 + j // 3

                if element in board_sets['row_sets'][i] or \
                   element in board_sets['col_sets'][j] or \
                   element in board_sets['square_sets'][square]: return False

                board_sets['row_sets'][i].add(element)
                board_sets['col_sets'][j].add(element)
                board_sets['square_sets'][square].add(element)

        return True
                