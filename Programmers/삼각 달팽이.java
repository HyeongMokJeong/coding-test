import java.util.LinkedList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        int[][] temp = new int[n][n];
        List<Integer> tempList = new LinkedList<>();

        int x = -1, y = 0;
        int count = 1;

        // i는 세트 반복 횟수, % 3을 통해 방향 판단
        for (int i = 0; i < n; i++) {
            // 하 - 우 - 좌상 반복될 때마다 depth 증가하기 때문에 j = i
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) x++;
                else if (i % 3 == 1) y ++;
                else if (i % 3 == 2) {
                    x--; 
                    y--;
                }
                temp[x][y] = count++;
            }
        }

        for (int[] te : temp) {
            for (int t : te) {
                if (t == 0) break;
                tempList.add(t);
            }
        }
        return tempList.stream().mapToInt(i -> i).toArray();
    }
}