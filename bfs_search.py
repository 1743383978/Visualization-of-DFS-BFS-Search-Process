import pygame
from collections import deque
import time

delay = 20  # 搜索动画延迟

def bfs_search(maze, start, end, win, CELL_WIDTH, CELL_HEIGHT, ROWS, COLS, offset_x=0):
    queue = deque([(start, [start])])
    visited = set()
    search_visited = []
    final_path = None
    current_pos = start
    total_steps = 0  # 总步数计数器
    
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        (x, y), path = queue.popleft()
        current_pos = (x, y)
        total_steps += 1  # 每访问一个格子，步数加1
        
        if (x, y) == end:
            final_path = path
            break
            
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        search_visited.append((x, y))
        
        # 绘制当前状态
        win.fill((234, 239, 242))  # 清屏
        for i in range(ROWS):
            for j in range(COLS):
                if maze[i][j] == 1:
                    rect = pygame.Rect(j * CELL_WIDTH + offset_x, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                    pygame.draw.rect(win, (255, 255, 255), rect)
        
        for vx, vy in visited:
            rect = pygame.Rect(vy * CELL_WIDTH + offset_x, vx * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(win, (200, 220, 240), rect)
            
        # 确保起点和终点在正确位置
        pygame.draw.circle(win, (40, 180, 99), 
                         (start[1] * CELL_WIDTH + CELL_WIDTH // 2 + offset_x, 
                          start[0] * CELL_HEIGHT + CELL_HEIGHT // 2), 8)
        pygame.draw.circle(win, (231, 76, 60), 
                         (end[1] * CELL_WIDTH + CELL_WIDTH // 2 + offset_x, 
                          end[0] * CELL_HEIGHT + CELL_HEIGHT // 2), 8)
        
        pygame.draw.circle(win, (50, 130, 255),
                         (y * CELL_WIDTH + CELL_WIDTH // 2 + offset_x,
                          x * CELL_HEIGHT + CELL_HEIGHT // 2), 4)
        
        # 绘制按钮区域
        pygame.draw.rect(win, (50, 50, 50), (0, win.get_height() - 80, win.get_width(), 80))
        
        # 更新显示
        pygame.display.update()
        pygame.time.delay(delay)
        
        # 添加邻居
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < ROWS and 0 <= ny < COLS and 
                maze[nx][ny] == 0 and (nx, ny) not in visited):
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return final_path, search_visited, total_steps