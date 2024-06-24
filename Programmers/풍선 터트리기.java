class Solution {
    public int solution(int[] a) {
        int answer = 2;

        int[] left = new int[a.length]; int[] right = new int[a.length];
        int l = a[0]; int r = a[a.length - 1];

        for (int i = 1; i < a.length; i++) {
            l = Math.min(l, a[i]);
            left[i] = l;
        }

        for (int i = a.length - 2; i > 0; i--) {
            r = Math.min(r, a[i]);
            right[i] = r;
        }

        for (int i = 1; i < a.length - 1; i++) {
            if (a[i] > left[i] && a[i] > right[i]) continue;
            answer++;
        }

        return answer;
    }
}