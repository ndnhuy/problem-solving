// https://www.hackerrank.com/challenges/castle-on-the-grid/problem
import java.util.ArrayList;
import java.util.List;

public class CastleOnTheGrid {

    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();
        queue.put(new Integer[] {1,2,3,4,5,6,7});
        queue.pop();
        queue.pop();
        queue.pop();
        queue.put(9);
        queue.put(10);
        queue.put(11);
        while (!queue.isEmpty()) {
            System.out.println(queue.pop());
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
            Path[] possiblePaths = findNextPossiblePathsFrom(path, visitedCells, grid2d);
            markAsVisitedPath(path, visitedCells);
            for (int i = 0; i < possiblePaths.length; i++) {
                possiblePaths[i].level = path.level + 1;
                queue.put(possiblePaths[i]);
            }
        }

        return -1;
    }

    private static void markAsVisitedPath(Path path, boolean[][] visitedCells) {

    }

    private static Path[] findNextPossiblePathsFrom(Path path, boolean[][] visitedCells, char[][] grid2d) {
        List<Path> paths = new ArrayList<>();
        // Horizontal path
        if (path.start.x == path.end.x) {
            int x = path.start.x;
            //TODO start does not always stay before end
            for (int y = path.start.y; y <= path.end.y; y++) {
                if (visitedCells[x][y]) {
                    continue;
                }
                paths.addAll(findPossiblePathsFrom(x, y, path.level, visitedCells, grid2d));
            }
        }
        return new Path[1];
    }

    private static List<Path> findPossiblePathsFrom(int x, int y, int level, boolean[][] visitedCells, char[][] grid2d) {
        List<Path> paths = new ArrayList<>();
        Cell startCell = new Cell(x, y);
        // Only pick a path that does not contain any visited cells

        // Look at the left
        int yIter = y - 1;
        boolean visitedCellFound = false;
        while (yIter >= 0 && grid2d[x][yIter] != 'x') {
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
        yIter = y + 1;
        visitedCellFound = false;
        while (yIter < grid2d.length && grid2d[x][yIter] != 'x') {
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
        int xIter = x - 1;
        visitedCellFound = false;
        while (xIter >= 0 && grid2d[xIter][y] != 'x') {
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
        xIter = x + 1;
        visitedCellFound = false;
        while (xIter < grid2d.length && grid2d[xIter][y] != 'x') {
            if (visitedCells[xIter][y]) {
                visitedCellFound = true;
                break;
            }
            xIter++;
        }
        if (!visitedCellFound) {
            paths.add(new Path(startCell, new Cell(xIter - 1, y), level));
        }
        return paths;
    }

    private static boolean reachTheGoal(Path path, int goalX, int goalY) {
        return true;
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
        }
    }
}
