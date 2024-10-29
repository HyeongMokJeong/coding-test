package SOFTEER;

import java.io.*;

class XmarksTheSpot {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            String s = input[0].toUpperCase();
            String[] t = input[1].split("");

            int idx = s.indexOf("X");
            sb.append(t[idx].toUpperCase());
        }
        System.out.println(sb.toString());
        br.close();
    }
}
