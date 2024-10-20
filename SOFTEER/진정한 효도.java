package SOFTEER;

import java.io.*;
import java.util.*;

class 진정한효도 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int size = 3;
        int[][] map = new int[size][size];
        for (int i = 0; i < size; i++) {
            int[] ary = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

            for (int j = 0; j < size; j++) map[i][j] = ary[j];
        }

        // 모든 조합(6가지)를 저장할 리스트 생성
        List<int[]> combi = new ArrayList<>();
        // 가로 3가지 추가
        for (int[] m : map) combi.add(m);
        //세로 3가지 추가
        for (int i = 0; i < size; i++) {
            int[] temp = new int[size];
            for (int j = 0; j < size; j++) temp[j] = map[j][i];
            combi.add(temp);
        }

        for (int[] c : combi) Arrays.sort(c);

        int result = Integer.MAX_VALUE;
        for (int[] c : combi) {
            if (c[0] == c[1] && c[1] == c[2]) {
                result = 0;
                break;
            }
            result = Math.min(result, c[2] - c[0] + c[2] - c[1]);
        }
        System.out.println(result);
        br.close();
    }
}
