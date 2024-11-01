package SOFTEER;

import java.io.*;
import java.util.*;

class 우물안개구리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // nm 입력
        int[] nm = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nm[0], m = nm[1];

        // 이미 패배한 상태인지 체크하는 check 배열 선언 및 W 배열 입력
        boolean[] check = new boolean[n];
        int[] w = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        // 아무런 친분이 없는 상태에서 시작
        int result = n;
        // 친분 입력
        for (int i = 0; i < m; i++) {
            // 인덱스로 활용할 것이기 때문에 각각 -1해서 배열로 입력
            int[] ab = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .map(t -> t - 1)
                .toArray();
            int a = ab[0], b = ab[1];
            
            // a b가 똑같다면?
            if (a == b) continue;

            // 둘이 무게가 같다면 둘 다 자신을 최고라고 생각하지 않음
            if (w[a] == w[b]){
                for (int target : ab) {
                    if (!check[target]) {
                        check[target] = true;
                        result -= 1;
                    }
                }
            }
            // 무게가 다르다면 더 적게 드는(자신을 최고라고 생각하지 않는) 사람 발생
            else {
                int minTarget = (w[b] > w[a]) ? a : b;

                // 자신을 최고라고 생각하고 있었다면 체크 후 결과값 반영
                if (!check[minTarget]) {
                    check[minTarget] = true;
                    result -= 1;
                }
            }
        }
        System.out.println(result);
        br.close();
    }
}
