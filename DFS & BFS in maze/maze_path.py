import pygame
import os

# 颜色配置
BG_COLOR = (234, 239, 242)
WALL_COLOR = (255, 255, 255)
PATH_COLOR = (50, 130, 255)
START_COLOR = (40, 180, 99)
END_COLOR = (231, 76, 60)
VISITED_COLOR = (200, 220, 240)
BUTTON_BG = (50, 50, 50)
BUTTON_COLOR = (180, 180, 180)
TEXT_COLOR = (255, 255, 255)
TEXT_COLOR_DARK = (0, 0, 0)

# 字体缓存
font_cache = {}
popup_font_cache = {}

def get_chinese_font(size, is_popup=False):
    """获取支持中文的字体"""
    cache = popup_font_cache if is_popup else font_cache
    if size in cache:
        return cache[size]
    
    chinese_fonts = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
    ]
    
    for font_path in chinese_fonts:
        if os.path.exists(font_path):
            try:
                font = pygame.font.Font(font_path, size)
                cache[size] = font
                return font
            except:
                continue
    
    try:
        font = pygame.font.SysFont("simhei,microsoft yahei,pingfang,Arial Unicode MS", size)
        cache[size] = font
        return font
    except:
        font = pygame.font.Font(None, size)
        cache[size] = font
        return font

def draw_maze(win, maze, path, visited_set, start, end, CELL_WIDTH, CELL_HEIGHT, offset_x=0):
    win.fill(BG_COLOR)
    ROWS = len(maze)
    COLS = len(maze[0])
    
    # 画墙
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == 1:
                rect = pygame.Rect(j * CELL_WIDTH + offset_x, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                pygame.draw.rect(win, WALL_COLOR, rect)

    # 画访问过的格子
    if visited_set:
        for vx, vy in visited_set:
            # 确保坐标在有效范围内
            if 0 <= vx < ROWS and 0 <= vy < COLS:
                rect = pygame.Rect(vy * CELL_WIDTH + offset_x, vx * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                pygame.draw.rect(win, VISITED_COLOR, rect)

    # 画路径
    if path and len(path) > 1:
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            # 确保坐标在有效范围内
            if (0 <= x1 < ROWS and 0 <= y1 < COLS and 
                0 <= x2 < ROWS and 0 <= y2 < COLS):
                pygame.draw.line(win, PATH_COLOR,
                                 (y1 * CELL_WIDTH + CELL_WIDTH // 2 + offset_x, 
                                  x1 * CELL_HEIGHT + CELL_HEIGHT // 2),
                                 (y2 * CELL_WIDTH + CELL_WIDTH // 2 + offset_x, 
                                  x2 * CELL_HEIGHT + CELL_HEIGHT // 2),
                                 5)

    # 起点终点 - 确保坐标在有效范围内
    if start and 0 <= start[0] < ROWS and 0 <= start[1] < COLS:
        sx, sy = start
        pygame.draw.circle(win, START_COLOR, 
                         (sy * CELL_WIDTH + CELL_WIDTH // 2 + offset_x, 
                          sx * CELL_HEIGHT + CELL_HEIGHT // 2), 8)
    if end and 0 <= end[0] < ROWS and 0 <= end[1] < COLS:
        ex, ey = end
        pygame.draw.circle(win, END_COLOR, 
                         (ey * CELL_WIDTH + CELL_WIDTH // 2 + offset_x, 
                          ex * CELL_HEIGHT + CELL_HEIGHT // 2), 8)


def draw_buttons(win, msg, steps, time_used, HEIGHT, BUTTON_HEIGHT):
    pygame.draw.rect(win, BUTTON_BG, (0, HEIGHT - BUTTON_HEIGHT, win.get_width(), BUTTON_HEIGHT))
    btn_w = 140
    btn_h = 45
    gap = 30
    x_start = 60
    y_start = HEIGHT - BUTTON_HEIGHT + (BUTTON_HEIGHT - btn_h) // 2

    rect_dfs = pygame.Rect(x_start, y_start, btn_w, btn_h)
    rect_bfs = pygame.Rect(x_start + btn_w + gap, y_start, btn_w, btn_h)
    rect_reset = pygame.Rect(x_start + 2 * (btn_w + gap), y_start, btn_w, btn_h)

    pygame.draw.rect(win, BUTTON_COLOR, rect_dfs)
    pygame.draw.rect(win, BUTTON_COLOR, rect_bfs)
    pygame.draw.rect(win, BUTTON_COLOR, rect_reset)

    font = get_chinese_font(28)
    dfs_text = font.render("DFS", True, TEXT_COLOR_DARK)
    bfs_text = font.render("BFS", True, TEXT_COLOR_DARK)
    reset_text = font.render("重新生成", True, TEXT_COLOR_DARK)
    
    win.blit(dfs_text, (rect_dfs.x + (btn_w - dfs_text.get_width()) // 2, rect_dfs.y + (btn_h - dfs_text.get_height()) // 2))
    win.blit(bfs_text, (rect_bfs.x + (btn_w - bfs_text.get_width()) // 2, rect_bfs.y + (btn_h - bfs_text.get_height()) // 2))
    win.blit(reset_text, (rect_reset.x + (btn_w - reset_text.get_width()) // 2, rect_reset.y + (btn_h - reset_text.get_height()) // 2))

    # 状态信息
    info = f"{msg}  步数: {steps if steps else '--'}  时间: {time_used:.3f}s"
    info_text = font.render(info, True, TEXT_COLOR)
    win.blit(info_text, (x_start + 3 * (btn_w + gap) + 50, y_start + 10))

    return rect_dfs, rect_bfs, rect_reset

def popup_message(surface, message_lines):
    WIDTH, HEIGHT = surface.get_size()
    w, h = 400, 200
    popup_rect = pygame.Rect((WIDTH - w) // 2, (HEIGHT - h) // 2, w, h)
    pygame.draw.rect(surface, (255, 255, 255), popup_rect)
    pygame.draw.rect(surface, (0, 0, 0), popup_rect, 3)

    popup_font = get_chinese_font(36, True)
    for idx, line in enumerate(message_lines):
        text_surf = popup_font.render(line, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(WIDTH // 2, (HEIGHT - h) // 2 + 40 + idx * 40))
        surface.blit(text_surf, text_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                waiting = False