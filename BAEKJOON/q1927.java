import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

public class q1927 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        PriorityQueue<Integer> q = new PriorityQueue<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int t = Integer.parseInt(br.readLine());
            if (t == 0){
                if (q.isEmpty()) bw.write("0\n");
                else bw.write(String.valueOf(q.poll()) + "\n");
            }
            else q.add(t);
        }
        bw.flush();
        br.close();
        bw.close();
    }
}