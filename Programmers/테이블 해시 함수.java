import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data, (o1, o2) -> o1[col - 1] != o2[col - 1] ? o1[col - 1] - o2[col - 1] : o2[0] - o1[0]);
        for (int i = row_begin - 1; i < row_end; i ++) {
            int temp = 0;
            for (int tar : data[i]) temp += tar % (i + 1);
            answer ^= temp;
        }
        return answer;
    }
}