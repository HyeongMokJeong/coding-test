package SOFTEER;

import java.io.*;
import java.util.*;

class 전광판 {
    static Map<Character, String> map = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        map.put('0', "1110111");
        map.put('1', "0010010");
        map.put('2', "1011101");
        map.put('3', "1011011");
        map.put('4', "0111010");
        map.put('5', "1101011");
        map.put('6', "1101111");
        map.put('7', "1110010");
        map.put('8', "1111111");
        map.put('9', "1111011");
        map.put(' ', "0000000");
        
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String[] ab = br.readLine().split(" ");

            char[] a = String.format("%5s", ab[0]).toCharArray();
            char[] b = String.format("%5s", ab[1]).toCharArray();

            int temp = 0;
            for (int j = 0; j < 5; j++) temp += run(a[j], b[j]);
            
            System.out.println(temp);
        }
        br.close();
    }

    private static int run(char a, char b) {
        String aValue = map.get(a), bValue = map.get(b);

        int result = 0;
        for (int i = 0; i < aValue.length(); i++) {
            if (aValue.charAt(i) != bValue.charAt(i)) result += 1;
        }

        return result;
    }
}
