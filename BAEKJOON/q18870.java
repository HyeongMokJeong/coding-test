import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class q18870 {
    public static void main(String args[]) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> ary = new ArrayList<>();
        ArrayList<Integer> temp = new ArrayList<>();
        HashMap<Integer, Integer> m = new HashMap<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < n; i++) {
            int t = Integer.parseInt(st.nextToken());
            ary.add(t);
            temp.add(t);
        }

        Collections.sort(temp);
        int count = 0;
        for (int i : temp) {
            if (m.get(i) == null) {
                m.put(i, count++);
            }
        }

        for (int i : ary) {
            bw.write(String.valueOf(m.get(i)) + " ");
        }
        bw.flush();
        bw.close();
    }
}
