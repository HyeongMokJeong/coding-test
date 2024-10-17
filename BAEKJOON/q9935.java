import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class q9935 {
    public static void main(String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        String target = br.readLine(); String boom = br.readLine();
        int tl = target.length(); int bl = boom.length();
    
        Stack<Character> stack = new Stack<>();
        for (char t : target.toCharArray()) {
            stack.push(t);
        
            int ss = stack.size();
            if (ss >= bl) {
                int count = 0;
                for (int j = 0; j < bl; j++) {
                    if (stack.get(ss - bl + j) == boom.charAt(j)) {
                        count += 1;
                    }
                }
                if (count == bl) {
                    for (int d = 0; d < bl; d++) {
                        stack.pop();
                    }
                }
            }
        }
        if (stack.isEmpty()) bw.write("FRULA");
            else {
                for (char t : stack) bw.write(t);
            }
            bw.flush();
            br.close(); bw.close();
    }
}
