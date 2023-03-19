import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.stream.Stream;

public class q1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<String> result = new ArrayList<>();
        HashMap<String, Integer> dic = new HashMap<>();

        int[] input = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = input[0], m = input[1];

        for (int i = 0; i < n; i++) {
            dic.put(br.readLine(), 1);
        }

        for (int i = 0; i < m; i++) {
            String name = br.readLine();
            if (dic.get(name) != null) result.add(name);
        }

        Collections.sort(result);
        bw.write(result.size() + "\n");
        for (String target : result) {
            bw.write(target + "\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}