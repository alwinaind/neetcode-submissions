class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if target > matrix[i][0]:
                if target > matrix[i][-1]:
                    continue
                elif target < matrix[i][-1]:
                    for j in range(0, len(matrix[i])):
                        if matrix[i][j] == target:
                            return True
                else:
                    return True
            elif target < matrix[i][0]:
                return False
            else:
                return True
        return False
