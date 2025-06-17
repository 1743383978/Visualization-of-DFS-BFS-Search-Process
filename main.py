import pygame
import time
from maze_init import generate_maze
from maze_path import draw_maze, draw_buttons, popup_message
from dfs_search import dfs_search
from bfs_search import bfs_search

WIDTH, HEIGHT = 1280, 720
BUTTON_HEIGHT = 80
MAZE_HEIGHT = HEIGHT - BUTTON_HEIGHT
COLS = 41  # 列数
ROWS = int(COLS * 0.5625)  # 保持宽高比

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("迷宫 - DFS / BFS made by ChenJR")
    
    maze, start, end = generate_maze(ROWS, COLS)
    # 获取实际迷宫尺寸
    ACTUAL_ROWS = len(maze)
    ACTUAL_COLS = len(maze[0])
    # 根据实际尺寸计算单元格大小
    CELL_WIDTH = min(WIDTH // ACTUAL_COLS, MAZE_HEIGHT // ACTUAL_ROWS)
    CELL_HEIGHT = CELL_WIDTH  # 保持单元格为正方形
    
    # 计算水平偏移量使迷宫居中
    MAZE_WIDTH = ACTUAL_COLS * CELL_WIDTH
    offset_x = (WIDTH - MAZE_WIDTH) // 2
    
    # 打印起点和终点位置（用于调试）
    print(f"Initial start: {start}, end: {end}")
    print(f"Actual maze dimensions: {ACTUAL_ROWS}x{ACTUAL_COLS}")
    print(f"Cell size: {CELL_WIDTH}x{CELL_HEIGHT}")
    print(f"Maze width: {MAZE_WIDTH}, offset: {offset_x}")
    
    status = "等待操作"
    path = []
    visited_cells = set()
    steps = 0
    time_used = 0

    running = True
    dfs_btn = bfs_btn = reset_btn = None

    while running:
        # 确保起点和终点在迷宫中正确显示
        draw_maze(win, maze, path, visited_cells, start, end, CELL_WIDTH, CELL_HEIGHT, offset_x)
        dfs_btn, bfs_btn, reset_btn = draw_buttons(win, status, steps, time_used, HEIGHT, BUTTON_HEIGHT)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if dfs_btn.collidepoint(x, y):
                    status = "DFS搜索中..."
                    path = []
                    visited_cells = set()
                    steps = 0
                    time_used = 0

                    t0 = time.time()
                    result_path, search_visited, total_steps = dfs_search(
                        maze, start, end, win, CELL_WIDTH, CELL_HEIGHT, ACTUAL_ROWS, ACTUAL_COLS, offset_x
                    )
                    time_used = time.time() - t0
                    
                    if result_path:
                        path = result_path
                        visited_cells = set(search_visited)
                        steps = total_steps
                        status = "已找到路径"
                        popup_message(win, [f"DFS搜索完成！", f"步数：{steps}", f"时间：{time_used:.3f}秒", "按任意键关闭"])
                    else:
                        visited_cells = set(search_visited)
                        status = "无解"

                elif bfs_btn.collidepoint(x, y):
                    status = "BFS搜索中..."
                    path = []
                    visited_cells = set()
                    steps = 0
                    time_used = 0

                    t0 = time.time()
                    result_path, search_visited, total_steps = bfs_search(
                        maze, start, end, win, CELL_WIDTH, CELL_HEIGHT, ACTUAL_ROWS, ACTUAL_COLS, offset_x
                    )
                    time_used = time.time() - t0
                    
                    if result_path:
                        path = result_path
                        visited_cells = set(search_visited)
                        steps = total_steps
                        status = "已找到路径"
                        popup_message(win, [f"BFS搜索完成！", f"步数：{steps}", f"时间：{time_used:.3f}秒", "按任意键关闭"])
                    else:
                        visited_cells = set(search_visited)
                        status = "无解"

                elif reset_btn.collidepoint(x, y):
                    maze, start, end = generate_maze(ROWS, COLS)
                    # 重新计算实际尺寸
                    ACTUAL_ROWS = len(maze)
                    ACTUAL_COLS = len(maze[0])
                    CELL_WIDTH = min(WIDTH // ACTUAL_COLS, MAZE_HEIGHT // ACTUAL_ROWS)
                    CELL_HEIGHT = CELL_WIDTH
                    MAZE_WIDTH = ACTUAL_COLS * CELL_WIDTH
                    offset_x = (WIDTH - MAZE_WIDTH) // 2
                    print(f"Reset - new start: {start}, end: {end}")  # 调试信息
                    path = []
                    visited_cells = set()
                    status = "等待操作"
                    steps = 0
                    time_used = 0

    pygame.quit()

if __name__ == "__main__":
    main()