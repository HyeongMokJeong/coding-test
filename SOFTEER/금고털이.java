package SOFTEER;

import java.io.*;
import java.util.*;

class 금고털이 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] wn = br.readLine().split(" ");
        int w = Integer.parseInt(wn[0]);
        int n = Integer.parseInt(wn[1]);

        List<int[]> jewels = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] mp = br.readLine().split(" ");
            int m = Integer.parseInt(mp[0]);
            int p = Integer.parseInt(mp[1]);
            jewels.add(new int[]{m, p});
        }
        // 가격이 큰 순으로 정렬
        jewels.sort((a, b) -> b[1] - a[1]);

        int result = 0;
        for (int[] jewel : jewels) {
            int m = jewel[0];
            int p = jewel[1];

            if (w >= m) {
                w -= m;
                result += m * p;
            } else {
                result += w * p;
                w = 0;
            }
            if (w == 0) break;
        }
        System.out.println(result);
        br.close();
    }
}
