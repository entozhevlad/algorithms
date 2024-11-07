class ShipStatus:
    def __init__(self):
        self.intact = 0
        self.damaged = 0
        self.destroyed = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def bfs(start_x, start_y, grid, visited):
    queue = [(start_x, start_y)]
    visited[start_x][start_y] = True
    hasX = False
    hasHash = False

    while queue:
        x, y = queue.pop(0)
        if grid[x][y] == 'X':
            hasX = True
        if grid[x][y] == '#':
            hasHash = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] in ('#', 'X'):
                visited[nx][ny] = True
                queue.append((nx, ny))

    return hasX, hasHash

def count_ships(grid):
    N, M = len(grid), len(grid[0])
    visited = [[False] * M for _ in range(N)]
    status = ShipStatus()

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] in ('#', 'X'):
                hasX, hasHash = bfs(i, j, grid, visited)

                if hasHash and not hasX:
                    status.intact += 1
                elif hasX and hasHash:
                    status.damaged += 1
                elif hasX and not hasHash:
                    status.destroyed += 1

    return status


n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

status = count_ships(grid)
print(status.intact, status.damaged, status.destroyed)


