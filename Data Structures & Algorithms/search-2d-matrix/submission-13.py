class Solution:
    def searchMatrix(self, matrix, target) :
        if not matrix :
            return False
        up = 0 
        down = len(matrix) - 1 
        mid = (up + down) // 2

        while up <= down :
            print(mid)
            mid = (up + down) // 2
            if matrix[mid][0] > target :
                down = mid - 1 
            elif matrix[mid][0] < target :
                up = mid + 1 
            else :
                return True
        if matrix[mid][0] > target :
            mid -= 1
        left = 0
        print(" i got here ")
        right = len(matrix[mid]) - 1
        while left <= right :
            print(right)
            print(left)
            print(mid)
            if left == right and matrix[mid][right] != target :
                return False
            mid1 = (left + right) // 2
            if matrix[mid][mid1] > target :
                right = mid1 - 1 
            elif matrix[mid][mid1] < target :
                left = mid1 + 1 
            else :
                return True
        return matrix[mid][left] == target 