"""bfs"""
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    n,m = len(mat), len(mat[0])
    queue = []
    queue = collections.deque(queue)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                queue.append((i,j))
    while queue:
        r,c = queue.popleft()
        for neighbor in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            i,j = neighbor
            if 0<=i<n and 0<=j<m and mat[i][j]==1:
                mat[i][j] = mat[r][c]-1
                queue.append((i,j))
    for i in range(n):
        for j in range(m):
            mat[i][j] *= -1
    return mat
