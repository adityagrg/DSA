class Solution:
    def _util(self, image, direction, i, j, m, n, color, visited):
            if i > 0 and direction != 'd':
                if image[i][j] == image[i-1][j] and (i-1, j) not in visited:
                    visited.add((i-1, j))
                    self._util(image, 'u', i-1, j, m, n, color, visited)
            
            if j < n-1 and direction != 'l':
                if image[i][j] == image[i][j+1] and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    self._util(image, 'r', i, j+1, m, n, color, visited)
            
            if i < m-1 and direction != 'u':
                if image[i][j] == image[i+1][j] and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    self._util(image, 'd', i+1, j, m, n, color, visited)

            if j > 0 and direction != 'r':
                if image[i][j] == image[i][j-1] and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    self._util(image, 'l', i, j-1, m, n, color, visited)
            
            image[i][j] = color

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        m = len(image)
        n = len(image[0])
        visited = set()
        visited.add((sr, sc))
        if sr > 0 and image[sr][sc] == image[sr-1][sc]:
            self._util(image, 'u', sr-1, sc, m, n, color, visited)
        
        if sc < n-1 and image[sr][sc] == image[sr][sc+1]:
            self._util(image, 'r', sr, sc+1, m, n, color, visited)

        if sr < m-1 and image[sr][sc] == image[sr+1][sc]:
            self._util(image, 'd', sr+1, sc, m, n, color, visited)
        
        if sc > 0 and image[sr][sc] == image[sr][sc-1]:
            self._util(image, 'l', sr, sc-1, m, n, color, visited)
        
        image[sr][sc] = color
        return image