class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        matrix = matrix
        max_rows = 0
        for now_row in matrix:
            reverse_row = [1-x for x in now_row]
            identical_row_count = sum(
                1
                for row in matrix
                if now_row == row or reverse_row == row
            )
            max_rows = max(max_rows,identical_row_count)

        return max_rows
            
            
