import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class q1256 {
    // dp[n][m] 은 "a" n개, "z" m개로 만들 수 있는 경우의 수
    static double[][] dp = new double[101][101];
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bf.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        double k = Double.parseDouble(inputs[2]);

        if (check(n, m) < k) {
            System.out.println("-1");
        } else {
            make(n, m, k);
            System.out.println(sb.toString());
        }
    }

    private static double check(int x, int y) {
        if (x == 0 || y == 0) return 1;
        if (dp[x][y] != 0) return dp[x][y];

        return dp[x][y] = Double.min(check(x - 1, y) + check(x, y - 1), 1000000001);
    }

    public static void make(int a, int z, double k) {
		if(a==0) {
			for(int i=0; i<z; i++)
				sb.append("z");
			return;
		}
		if(z==0) {
			for(int i=0; i<a; i++)
				sb.append("a");
			return;
		}
		
		double check= check(a-1, z);
		if(k>check) {
			sb.append("z");
			make(a, z-1, k-check);
		}else {
			sb.append("a");
			make(a-1, z, k);
		}
	}
}