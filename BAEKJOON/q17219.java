import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.stream.Stream;

public class q17219 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<String, String> map = new HashMap<>();
        int[] nm = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        for (int i = 0; i < nm[0]; i++) {
            String[] ary = br.readLine().split(" ");
            map.put(ary[0], ary[1]);
        }

        for (int i = 0; i < nm[1]; i++) {
            String target = br.readLine();
            bw.write(map.get(target) + '\n');
        }

        bw.flush();
        br.close();
        bw.close();
    }
}