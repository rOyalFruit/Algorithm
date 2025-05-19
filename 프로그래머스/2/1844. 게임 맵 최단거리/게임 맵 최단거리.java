import java.util.*;

class Solution {
    class Pos{
        int i;
        int j;

        public Pos(int i, int j){
            this.i = i;
            this.j = j;
        }
    }

    public int bfs(Pos start, int[][] maps){
        Queue<Pos> q = new LinkedList<>();
        int n = maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        int[] dy = new int[]{1, -1, 0, 0};
        int[] dx = new int[]{0, 0, 1, -1};

        q.offer(start);
        visited[start.i][start.j] = 1;

        while(!q.isEmpty()){
            Pos cur = q.poll();

            if(cur.i == n-1 && cur.j == m-1){
                return visited[cur.i][cur.j];
            }

            for(int d = 0; d < 4; d++){
                int ni = cur.i + dy[d];
                int nj = cur.j + dx[d];

                if(0 <= ni && ni < n &&
                        0 <= nj && nj < m &&
                        maps[ni][nj] == 1 && visited[ni][nj] == 0){
                    q.offer(new Pos(ni, nj));
                    visited[ni][nj] = visited[cur.i][cur.j] + 1;
                }
            }
        }

        return -1;
    }

    public int solution(int[][] maps) {
        // 시작 위치는 (1, 1)이지만 2차원 배열에 적용하려면 (0, 0)이 되기 때문
        int answer = bfs(new Pos(0, 0), maps);
        
        return answer;
    }
}