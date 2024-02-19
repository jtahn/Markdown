def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:          # avoid infinite loop, if startCoord is already newColor
        return image
    
    x, y = len(image), len(image[0])    # need later: to check whether coord is in bounds
    oldColor = image[sr][sc]            # need later: to check whether coord is oldColor

    # only push oldColor, so no need to track visited aka newColor
    stack = [(sr,sc)]   # queue = collections.deque([(sr,sc)])
    while stack:        # while queue:
        r,c = stack.pop()   # queue.popleft()
        image[r][c] = color     
        for coord in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            i,j=coord
            if 0<=i<x and 0<=j<y and image[i][j]==oldColor:
                stack.append(coord)
    return image
