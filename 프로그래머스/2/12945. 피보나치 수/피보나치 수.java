class Solution {
    public int solution(int n) {
        int[] lst = new int[n+2];
        lst[1] = 1;

        for(int i = 2; i <= n; i++){
            lst[i] = (lst[i - 1] + lst[i - 2]) % 1234567;
        }

        return lst[n];
    }
}