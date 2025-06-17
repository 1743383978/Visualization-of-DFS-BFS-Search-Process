import random

def generate_maze(ROWS, COLS):
    # 确保行列数为奇数
    ROWS = ROWS * 2 - 1
    COLS = COLS * 2 - 1
    
    maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]
    visited = [[False] * COLS for _ in range(ROWS)]

    def dfs(x, y):
        visited[x][y] = True
        maze[x][y] = 0
        
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny]:
                maze[x + dx//2][y + dy//2] = 0
                dfs(nx, ny)

    # 从中心开始生成迷宫
    start_x = 1
    start_y = 1
    dfs(start_x, start_y)

    # 随机打通一些墙壁来创建更多路径
    extra_paths = int((ROWS * COLS) * 0.15)
    for _ in range(extra_paths):
        x = random.randint(1, ROWS-2)
        y = random.randint(1, COLS-2)
        if maze[x][y] == 1:
            paths_around = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] == 0:
                    paths_around += 1
            
            if paths_around >= 1:
                maze[x][y] = 0

    # 设置起点和终点
    # 选择起点（左边缘中间位置）
    start_x = ROWS // 2
    start_y = 1  # 从第1列开始
    
    # 确保起点左侧（包括左上和左下）都是墙
    maze[start_x][start_y] = 0  # 起点设为通路
    maze[start_x][0] = 1  # 起点正左侧设为墙
    maze[start_x-1][0] = 1  # 起点左上设为墙
    maze[start_x+1][0] = 1  # 起点左下设为墙
    start = (start_x, start_y)

    # 选择终点（右边缘中间位置）
    end_x = ROWS // 2
    end_y = COLS - 2  # 从倒数第2列开始
    
    # 确保终点右侧（包括右上和右下）都是墙
    maze[end_x][end_y] = 0  # 终点设为通路
    maze[end_x][COLS-1] = 1  # 终点正右侧设为墙
    maze[end_x-1][COLS-1] = 1  # 终点右上设为墙
    maze[end_x+1][COLS-1] = 1  # 终点右下设为墙
    end = (end_x, end_y)

    # 确保起点和终点周围有足够的空间
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # 起点周围
            nx, ny = start[0] + dx, start[1] + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                # 跳过起点左侧的墙
                if not (ny == 0 and nx in [start_x-1, start_x, start_x+1]):
                    maze[nx][ny] = 0
            
            # 终点周围
            nx, ny = end[0] + dx, end[1] + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                # 跳过终点右侧的墙
                if not (ny == COLS-1 and nx in [end_x-1, end_x, end_x+1]):
                    maze[nx][ny] = 0

    # 打印起点和终点的坐标（调试）
    print(f"Start position: {start}")
    print(f"End position: {end}")
    print(f"Maze dimensions: {ROWS}x{COLS}")

    return maze, start, end