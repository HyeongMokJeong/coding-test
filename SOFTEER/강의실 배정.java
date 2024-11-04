package SOFTEER;

import java.io.*;
import java.util.*;

class 강의실배정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] lectures = new int[n][2];
        for (int i = 0; i < n; i++) {
            int[] sf = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            lectures[i] = new int[]{sf[0], sf[1]};
        }
        Arrays.sort(lectures, (a, b) -> (a[0] == b[0]) ? b[1] - a[1] : b[0] - a[0]);

        int result = 0;
        int start = 0, end = 0;
        for (int[] lecture : lectures) {
            System.out.println(lecture[0] + " " + lecture[1]);
            int s = lecture[0], f = lecture[1];
            if (start == 0 && end == 0) {
                start = s;
                end = f;
                result += 1;
            } else {
                if (s >= end) {
                    end = f;
                    result += 1;
                }
            }
        }
        System.out.println(result);
        br.close();
    }
}
