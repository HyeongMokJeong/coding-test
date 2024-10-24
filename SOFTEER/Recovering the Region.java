package SOFTEER;

import java.io.*;
import java.util.*;

class RTR {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력값 저장
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) System.out.print((i + 1) + " ");
            System.out.println();
        }
        
        br.close();
    }
}
