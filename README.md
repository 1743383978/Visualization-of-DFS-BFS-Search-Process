# DFS & BFS 搜索过程可视化
# Visualization-of-DFS-BFS-Search-Process

利用Python PyGame对DFS & BFS在路径中的搜索过程进行可视化

Visualize the search process of DFS & BFS in the path using Python Pygame

## 概述 / Overview

该应用程序生成一个随机迷宫，并可视化 DFS 和 BFS 算法寻找从指定起点到终点的路径。迷宫使用 Pygame 显示，带有触发 DFS、BFS 或重置迷宫的按钮。可视化内容通过不同颜色高亮显示墙壁、路径、已访问的格子以及起点和终点。

The application generates a random maze and visualizes the DFS and BFS algorithms to find a path from a designated start to an end point. The maze is displayed using Pygame, with buttons to trigger DFS, BFS, or reset the maze. The visualization highlights walls, paths, visited cells, and start/end points with distinct colors.

## 安装 / Installation

```bash
pip install pygame
```
## 运行 / Running

运行 `main.py` 来启动程序  
Run `main.py` to start the program

## 使用方法 / Usage


1. 运行 `main.py` 启动应用程序。
2. 点击“DFS”或“BFS”按钮可视化相应的路径搜索算法。
3. 点击“重新生成”生成新迷宫。
4. 当找到路径或无解时，弹出窗口显示步数和耗时。
5. 关闭窗口或按键/鼠标按钮关闭弹出窗口。

**English**:
1. Run `main.py` to start the application.
2. Click the "DFS" or "BFS" button to visualize the respective pathfinding algorithm.
3. Click "Regenerate" to generate a new maze.
4. A popup appears when a path is found or no solution exists, showing steps and time taken.
5. Close the window or press a key/mouse button to dismiss popups.

## 界面翻译 / Interface Translation

| 中文 | English |
|------|---------|
| 重新生成 | Regenerate |
| 等待操作 | Waiting to Start |
| 搜索完成 | Searching Complete |
| 步数 | Steps |
| 时间 | Time |
| 已找到路径 | Path Found |
| 未找到路径 | Path Not Found |
| 按任意键关闭 | Press any key to close |

## 运行结果 / Running Result

运行结果如下图所示  
The running result is shown in the following figure

![image text](https://github.com/1743383978/Visualization-of-DFS-BFS-Search-Process/blob/main/running%20result/maze1.png)  
![image text](https://github.com/1743383978/Visualization-of-DFS-BFS-Search-Process/blob/main/running%20result/maze2.png)


### 算法描述 / Algorithm Description

迷宫使用带有随机回溯的 深度优先搜索（DFS） 算法生成，确保生成一个完美迷宫（任意两点之间只有一条路径），并通过添加随机路径增加复杂性。

The maze is generated using a **Depth-First Search (DFS)** approach with a randomized backtracking algorithm. This ensures a perfect maze (exactly one path between any two points) with additional random paths for complexity.

#### 迷宫生成步骤 / Steps in Maze Generation

1. **初始化**：
   - 迷宫尺寸调整为奇数（`ROWS * 2 - 1`, `COLS * 2 - 1`），以创建由墙壁分隔的格子网格。
   - 初始化一个所有格子均为墙壁（`1`）的网格。
   - 使用 `visited` 数组跟踪生成过程中已探索的格子。
2. **基于 DFS 的迷宫生成**：
   - 从一个格子（通常为 `(1, 1)`）开始，标记为路径（`0`），并递归探索邻居格子。
   - 从四个方向（上、下、左、右，步长为 2 以考虑墙壁）随机选择邻居。
   - 对于每个有效邻居（在边界内且未访问），移除当前格子与邻居之间的墙壁（设为 `0`），并从邻居继续探索。
   - 此过程生成一个生成树，确保迷宫完美无环。
3. **添加额外路径**：
   - 为增加复杂性，随机移除约 15% 的墙壁。
   - 仅当墙壁连接至少一个现有路径时才移除，以避免孤立开口。
4. **设置起点和终点**：
   - **起点**：位于左边缘中间行（`(ROWS // 2, 1)`），设为路径（`0`），左侧、左上、左下设为墙壁（`1`），定义清晰入口。
   - **终点**：位于右边缘倒数第二列（`(ROWS // 2, COLS - 2)`），设为路径（`0`），右侧、右上、右下设为墙壁（`1`），定义清晰出口。
   - 起点和终点周围区域（除入口/出口墙壁外）被清空以确保可达性。
5. **调试输出**：
   - 打印起点和终点坐标以及迷宫尺寸以供验证。

**English**:
1. **Initialization**:
   - The maze dimensions are adjusted to odd numbers (`ROWS * 2 - 1`, `COLS * 2 - 1`) to create a grid where cells are separated by walls.
   - A grid is initialized with all cells set to walls (`1`).
   - A `visited` array tracks explored cells during generation.
2. **DFS-Based Maze Generation**:
   - Starting from a cell (typically at `(1, 1)`), the algorithm marks it as a path (`0`) and recursively explores neighbors.
   - Neighbors are selected randomly from four directions: up, down, left, right (with a step of 2 to account for walls).
   - For each valid neighbor (within bounds and unvisited), the wall between the current cell and the neighbor is removed (set to `0`), and the algorithm continues from the neighbor.
   - This process creates a spanning tree, ensuring a perfect maze with no loops.
3. **Adding Extra Paths**:
   - To increase complexity, approximately 15% of the maze's cells are considered for wall removal.
   - A wall is removed only if it connects to at least one existing path, preventing isolated openings.
4. **Setting Start and End Points**:
   - **Start Point**: Located at the left edge, middle row (`(ROWS // 2, 1)`). The start cell is set to a path (`0`), with surrounding cells (left, top-left, bottom-left) set to walls (`1`) to define a clear entrance.
   - **End Point**: Located at the right edge, second-to-last column (`(ROWS // 2, COLS - 2)`). The end cell is set to a path (`0`), with surrounding cells (right, top-right, bottom-right) set to walls (`1`) to define a clear exit.
   - Both start and end points have their surrounding areas (except the entrance/exit walls) cleared to ensure accessibility.
5. **Debugging Output**:
   - The algorithm prints the start and end coordinates and maze dimensions for verification.

## 可视化 (`maze_path.py`) / Visualization (`maze_path.py`)

### 功能 / Functionality

`maze_path.py` 模块使用 Pygame 处理迷宫渲染、路径搜索可视化和用户界面元素，包括绘制迷宫、按钮和弹出消息的函数。

The `maze_path.py` module handles the rendering of the maze, pathfinding visualization, and user interface elements using Pygame. It includes functions to draw the maze, buttons, and popup messages.

## 与路径搜索的集成 / Integration with Pathfinding


- **DFS/BFS 搜索**（来自 `dfs_search.py` 和 `bfs_search.py`）：
  - 两种算法使用由 `maze_init.py` 生成的迷宫。
  - 通过更新显示（通过 `maze_path.py`）可视化每个已访问格子的搜索过程。
  - 返回最终路径、已访问格子和总步数以进行渲染。
- **主循环**（来自 `main.py`）：
  - 集成迷宫生成和可视化。
  - 处理用户输入以触发 DFS、BFS 或重置。
  - 使用 `maze_path.py` 绘制迷宫和按钮，确保渲染一致。

**English**:
- **DFS/BFS Search** (from `dfs_search.py` and `bfs_search.py`):
  - Both algorithms use the maze generated by `maze_init.py`.
  - They visualize the search process by updating the display (via `maze_path.py`) for each visited cell.
  - The final path, visited cells, and total steps are returned for rendering.
- **Main Loop** (from `main.py`):
  - Integrates maze generation and visualization.
  - Handles user input to trigger DFS, BFS, or reset.
  - Uses `maze_path.py` to draw the maze and buttons, ensuring consistent rendering.
