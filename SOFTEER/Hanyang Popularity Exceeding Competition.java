package SOFTEER;

import java.io.*;
import java.util.*;

class HPEC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int result = 0;
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int[] pc = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int p = pc[0], c = pc[1];

            // 유명인들과 만나는 순서를 변경할 수는 없다. ->
            // i - 1번째 유명인을 만나서 인기도를 1 올리고 i번째 유명인을 만나든,
            // i - 1번째 유명인을 건너뛰고 i번째 유명인을 만나서 인기도를 올리든 결과적으로는 같다.
            if (Math.abs(p - result) <= c) result += 1;
        }
        System.out.println(result);
        br.close();
    }
}
