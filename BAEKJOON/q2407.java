import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.util.stream.Stream;

public class q2407 {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] input = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = input[0], m = input[1];
        
        BigInteger num1 = BigInteger.ONE;
        BigInteger num2 = BigInteger.ONE;

        for (int i = 0; i < m; i++) {
            num1 = num1.multiply(new BigInteger(String.valueOf(n - i)));
            num2 = num2.multiply(new BigInteger(String.valueOf(i + 1)));
        }

        bw.write(String.valueOf(num1.divide(num2)));
        bw.flush();
        br.close();
        bw.close();
    }
}
