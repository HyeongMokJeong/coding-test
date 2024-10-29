package SOFTEER;

import java.io.*;

class 지도자동구축 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        // 행의 크기는 2의 n승 (2**n * 2**n개로 나눠진 정사각형이 나온다.)
        int count = (int) Math.pow(2, n);

        // 점의 개수는 (행의 크기 + 1)의 제곱
        System.out.println((int) Math.pow(count + 1, 2));
        br.close();
    }
}
