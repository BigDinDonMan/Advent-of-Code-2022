import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Arrays;

public class Main {
    static int[][] buildGrid(String inputPath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(inputPath));
        int[][] treeGrid = new int[lines.size()][lines.get(0).length()];
        for (int i = 0; i < lines.size(); ++i) {
            char[] chars = lines.get(i).toCharArray();
            for (int j = 0; j < chars.length; ++j) {
                treeGrid[i][j] = Integer.parseInt(Character.toString(chars[j]));
            }
        }
        return treeGrid;
    }

    static boolean isTreeVisible(int[][] treeGrid, int x, int y) {
        int currentCell = treeGrid[y][x];
        if (currentCell == 0) {
            return false;
        }

        boolean v1 = true, v2 = true, v3 = true, v4 = true;

        for (int i = 0; i < x; ++i) {
            if (currentCell <= treeGrid[y][i]){
                v1 = false;
                break;
            }
        }

        for (int i = x + 1; i < treeGrid[y].length; ++i) {
            if (currentCell <= treeGrid[y][i]){
                v2 = false;
                break;
            }
        }

        for (int i = 0; i < y; ++i) {
            if (currentCell <= treeGrid[i][x]){
                v3 = false;
                break;
            }
        }

        for (int i = y + 1; i < treeGrid.length; ++i) {
            if (currentCell <= treeGrid[i][x]){
                v4 = false;
                break;
            }
        }

        return v1 || v2 || v3 || v4;
    }

    static void printDebug(int[][] grid) {
        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[0].length; ++j) {
                System.out.printf("%d ", grid[i][j]);
            }
            System.out.println();
        }
    }

    static int getVisibleTrees(int[][] grid) {
        int result = 0;

        //edges are visible
        result += grid.length * 2;
        //again, edges are visible but 4 of the trees are already counted (corners)
        result += grid[0].length * 2 - 4;

        for (int i = 1; i < grid.length - 1; ++i) {
            for (int j = 1; j < grid[0].length - 1; ++j) {
                boolean visible = isTreeVisible(grid, j, i);
                result += visible ? 1 : 0;
            }
        }

        return result;
    }

    static int computeScenicScore(int[][] treeGrid, int x, int y) {
        int currentCell = treeGrid[y][x];
        if (currentCell == 0) {
            return 0;
        }

        int s1 = 0, s2 = 0, s3 = 0, s4 = 0;

        for (int i = x - 1; i >= 0; --i) {
            s1++;
            if (currentCell <= treeGrid[y][i]){
                break;
            }
        }

        for (int i = x + 1; i < treeGrid[y].length; ++i) {
            s2++;
            if (currentCell <= treeGrid[y][i]){
                break;
            }
        }

        for (int i = y-1; i >= 0; --i) {
            s3++;
            if (currentCell <= treeGrid[i][x]){
                break;
            }
        }

        for (int i = y + 1; i < treeGrid.length; ++i) {
            s4++;
            if (currentCell <= treeGrid[i][x]){
                break;
            }
        }

        return s1 * s2 * s3 * s4;
    }

    static int getMax(int[][] array) {
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < array.length; ++i) {
            for (int j = 0 ; j < array[0].length; ++j) {
                if (array[i][j] > max) {
                    max = array[i][j];
                }
            }
        }
        return max;
    }

    static int getHighestScenicScore(int[][] grid) {
        int[][] scoresGrid = new int[grid.length][grid[0].length];
        for (int i = 1; i < grid.length; ++i) {
            for (int j = 1; j < grid[0].length; ++j) {
                int score = computeScenicScore(grid, j, i);
                scoresGrid[i][j] = score;
            }
        }

        return getMax(scoresGrid);
    }

    public static void main(String[] args) {
        try {
            int[][] treeGrid = buildGrid("input.txt");

            int part1Result = getVisibleTrees(treeGrid);
            int part2Result = getHighestScenicScore(treeGrid);
            System.out.printf("Result for part 1: %d\n", part1Result);
            System.out.printf("Result for part 2: %d\n", part2Result);
        } catch (IOException e) {
            System.err.println("Whoops, something not working. Probably no file provided.");
        }
    }
}
