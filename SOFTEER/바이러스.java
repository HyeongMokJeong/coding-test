package SOFTEER;

import java.io.*;
import java.util.*;

class 바이러스 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        long k = input[0], p = input[1], n = input[2];

        for(int i = 0; i < n; i++) k = (k * p) % 1000000007;
        System.out.println(k);

        br.close();
    }
}
