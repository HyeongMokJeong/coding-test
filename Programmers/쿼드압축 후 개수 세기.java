class Solution {
    int countZero = 0; int countOne = 0;

    public int[] solution(int[][] arr) {
        run(arr, arr.length, 0, 0);
        return new int[]{countZero, countOne};
    }

    private void run(int[][] arr, int size, int x, int y) {
        int check = check(arr, x, y, size);
        if (check != -1) {
            if (check == 0) countZero++;
            else countOne++;
            return;
        }

        run(arr, size / 2, x, y);
        run(arr, size  / 2, x, y + size / 2);
        run(arr, size  / 2, x + size / 2, y);
        run(arr, size  / 2, x + size / 2, y + size / 2);
    }

    private int check(int[][] arr, int x, int y, int size) {
        int temp = arr[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (arr[i][j] != temp) return -1;
            }
        }
        return temp;
    }
}