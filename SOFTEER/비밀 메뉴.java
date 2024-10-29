package SOFTEER;

import java.io.*;

class 비밀메뉴 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String secret = br.readLine().replace(" ", "");
        String input = br.readLine().replace(" ", "");
        
        System.out.println((input.contains(secret)) ? "secret" : "normal");
        br.close();
    }
}
