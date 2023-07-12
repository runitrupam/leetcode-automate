class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel_curr_colr = image[sr][sc]
        m = len(image) # no of rows
        n = len(image[0]) # no of cols
        def ff(r,c):
            if r < 0 or c<0 or r >= m or c >= n :
                return
            if image[r][c] == color:
                return
            else:
                image[r][c] = color 

            if r+1 < m and image[r+1][c] == pixel_curr_colr :
                ff(r+1,c)
            if r-1 >= 0 and image[r-1][c] == pixel_curr_colr :
                ff(r-1,c)
            if c-1 >= 0 and image[r][c-1] == pixel_curr_colr :
                ff(r,c-1)
            if c+1 < n and image[r][c+1] == pixel_curr_colr :
                ff(r,c+1)
        ff(sr,sc)
        return image
            