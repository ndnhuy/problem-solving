// https://www.hackerrank.com/challenges/castle-on-the-grid/problem
import java.util.ArrayList;
import java.util.List;

public class CastleOnTheGrid {
    public static void main(String[] args) {
        int rs = minimumMoves(new String[] {
                "XXXXXXX",
                "......X",
                ".XXXX.X",
                "...XX.X",
                "...XX..",
                "...XX..",
                "...X..X"
        }, 6, 1, 6, 4);
        System.out.println(rs);
    }

    public static int minimumMoves(String[] grid, int startX, int startY, int goalX, int goalY) {
        char[][] grid2d = new char[grid.length][grid.length];
        for (int i = 0; i < grid.length; i++) {
            grid2d[i] = grid[i].toCharArray();
        }
        boolean[][] visitedCells = new boolean[grid.length][grid.length];
        Queue<Path> queue = new Queue<>();
        Cell startCell = new Cell(startX, startY);
        queue.put(new Path(startCell, startCell, 0));
        while (!queue.isEmpty()) {
            Path path = queue.pop();
            if (reachTheGoal(path, goalX, goalY)) {
                return path.level;
            }
            List<Path> possiblePaths = findNextPossiblePathsFrom(path, visitedCells, grid2d);
            queue.put(possiblePaths.toArray(new Path[]{}));
        }

        return -1;
    }

    private static List<Path> findNextPossiblePathsFrom(Path path, boolean[][] visitedCells, char[][] grid2d) {
        List<Path> paths = new ArrayList<>();
        for (Cell cell : findCellsOnPath(path)) {
            paths.addAll(findPossiblePathsFrom(cell, path.level, visitedCells, grid2d));
        }
        return paths;
    }

    private static List<Cell> findCellsOnPath(Path path) {
        List<Cell> cells = new ArrayList<>();
        // Horizontal path
        if (path.start.x == path.end.x) {
            int x = path.start.x;
            if (path.start.y <= path.end.y) {
                for (int i = path.start.y; i <= path.end.y; i++) {
                    cells.add(new Cell(x, i));
                }
            } else {
                for (int i = path.start.y; i >= path.end.y; i--) {
                    cells.add(new Cell(x, i));
                }
            }
            return cells;
        }

        // Vertical path
        if (path.start.y == path.end.y) {
            int y = path.start.y;
            if (path.start.x <= path.end.x) {
                for (int i = path.start.x; i <= path.end.x; i++) {
                    cells.add(new Cell(i, y));
                }
            } else {
                for (int i = path.start.x; i >= path.end.x; i--) {
                    cells.add(new Cell(i, y));
                }
            }
            return cells;
        }

        throw new RuntimeException("Only support horizontal or vertical path");
    }

    private static List<Path> findPossiblePathsFrom(Cell startCell, int currentLevel, boolean[][] visitedCells, char[][] grid2d) {
        List<Path> paths = new ArrayList<>();
        int level = currentLevel + 1;
        int x = startCell.x;
        int y = startCell.y;

        if (grid2d[x][y] == 'X' || visitedCells[x][y]) {
            return paths;
        }

        // Only pick a path that does not contain any visited cells
        // Look at the left
        int yIter = y;
        boolean visitedCellFound = false;
        while (yIter >= 0 && grid2d[x][yIter] != 'X') {
            if (visitedCells[x][yIter]) {
                visitedCellFound = true;
                break;
            }
            yIter--;
        }
        if (!visitedCellFound) {
            paths.add(new Path(startCell, new Cell(x, yIter + 1), level));
        }

        // Look at the right
        yIter = y;
        visitedCellFound = false;
        while (yIter < grid2d.length && grid2d[x][yIter] != 'X') {
            if (visitedCells[x][yIter]) {
                visitedCellFound = true;
                break;
            }
            yIter++;
        }
        if (!visitedCellFound) {
            paths.add(new Path(startCell, new Cell(x, yIter - 1), level));
        }

        // Up
        int xIter = x;
        visitedCellFound = false;
        while (xIter >= 0 && grid2d[xIter][y] != 'X') {
            if (visitedCells[xIter][y]) {
                visitedCellFound = true;
                break;
            }
            xIter--;
        }
        if (!visitedCellFound) {
            paths.add(new Path(startCell, new Cell(xIter + 1, y), level));
        }

        // Down
        xIter = x;
        visitedCellFound = false;
        while (xIter < grid2d.length && grid2d[xIter][y] != 'X') {
            if (visitedCells[xIter][y]) {
                visitedCellFound = true;
                break;
            }
            xIter++;
        }
        if (!visitedCellFound) {
            paths.add(new Path(startCell, new Cell(xIter - 1, y), level));
        }

        visitedCells[x][y] = true;
        return paths;
    }

    private static boolean reachTheGoal(Path path, int goalX, int goalY) {
        return isBetween(goalX, path.start.x, path.end.x) && isBetween(goalY, path.start.y, path.end.y);
    }

    private static boolean isBetween(int m, int p1, int p2) {
        return m >= Math.min(p1, p2) && m <= Math.max(p1, p2);
    }

    public static class Queue<E> {
        private static final int DEFAULT_SIZE = 8;

        private Object[] circularArr;
        private int head;
        private int tail;

        public Queue() {
            this(DEFAULT_SIZE);
        }

        public Queue(int size) {
            int capacity = size > DEFAULT_SIZE ? size : DEFAULT_SIZE;
            capacity |= (capacity >> 1);
            capacity |= (capacity >> 2);
            capacity |= (capacity >> 4);
            capacity |= (capacity >> 8);
            capacity |= (capacity >> 16);
            capacity++;
            if (capacity < 0) {
                capacity = capacity >> 1;
            }
            circularArr = new Object[capacity];
        }

        public void put(E[] values) {
            for (int i = 0; i < values.length; i++) {
                put(values[i]);
            }
        }

        public void put(E value) {
            circularArr[tail] = value;
            tail = (tail + 1) & (circularArr.length - 1);
            doubleCapacityIfFull();
        }

        public E pop() {
            Object result = circularArr[head];
            head = (head + 1) & (circularArr.length - 1);
            return (E) result;
        }

        public boolean isEmpty() {
            return head == tail;
        }

        private void doubleCapacityIfFull() {
            if (head != tail) {
                // the queue is not full
                return;
            }
            int n = circularArr.length;
            Object[] newArr = new Object[circularArr.length*2];
            int headToEnd = n - head;
            System.arraycopy(circularArr, head, newArr, 0, headToEnd);
            System.arraycopy(circularArr, 0, newArr, headToEnd, tail);
            circularArr = newArr;
            tail = n;

            // Forgot to update the head here that made 6 test cases fail and it took me over an hour to figure this shit out!!!!!!
            head = 0;
        }
    }

    public static class Cell {
        final int x;
        final int y;

        public Cell(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class Path {
        final Cell start;
        final Cell end;
        int level;

        public Path(Cell start, Cell end) {
            this.start = start;
            this.end = end;
        }

        public Path(Cell start, Cell end, int level) {
            this.start = start;
            this.end = end;
            this.level = level;
        }
    }
}
