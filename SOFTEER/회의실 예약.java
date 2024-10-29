package SOFTEER;

import java.io.*;
import java.util.*;

class 회의실예약 {    
    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int[] nm = Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt)
        .toArray();
    int n = nm[0], m = nm[1];

    List<String> nameList = new ArrayList<>();
    Map<String, boolean[]> timeMap = new HashMap<>();
    for (int i = 0; i < n; i++) {
        String name = br.readLine();
        nameList.add(name);
        timeMap.put(name, new boolean[9]);
    }
    Collections.sort(nameList);

    for (int i = 0; i < m; i++) {
        String[] input = br.readLine().split(" ");
        String key = input[0];
        int s = Integer.parseInt(input[1]), e = Integer.parseInt(input[2]);

        boolean[] time = timeMap.get(key);
        for (int j = s - 9; j < e - 9; j++) time[j] = true;
    }

    StringBuilder sb = new StringBuilder();
    for (String name : nameList) {
        sb.append("Room ").append(name).append(":").append("\n");
        int start = 0, end = 0;
        
        boolean[] time = timeMap.get(name);
        List<String> temp = new ArrayList<>();
        for (int i = 0; i < time.length; i++) {
            // 해당 시간에 예약이 된 경우
            if (time[i]) {
                // 기존에 비어있는 시간을 계산중이었다면
                if (start != 0) {
                    // 시간대 저장 후 초기화
                    temp.add(createString(start, end));
                    start = 0;
                }
            }
            // 예약이 가능한 경우
            else {
                // 첫 예약이라면
                if (start == 0) {
                    start = i + 9;
                    end = start + 1;
                }
                // 이어지고 있다면
                else end += 1;
            }
        }

        // 누락된 마지막 구간 처리
        if (start != 0) temp.add(createString(start, end));

        // 카운트, 시간 출력
        int count = temp.size();
        if (count == 0) sb.append("Not available\n");
        else {
            sb.append(count).append(" available:\n");
            for (String t : temp) sb.append(t).append("\n");
        }

        if (!name.equals(nameList.get(nameList.size() - 1))) sb.append("-----\n");
    }

    System.out.print(sb.toString());
    br.close();
}

private static String createString(int s, int e) {
    StringBuilder sb = new StringBuilder();
    if (s == 9) sb.append("0");
    sb.append(s).append("-").append(e);

    return sb.toString();
}
}
