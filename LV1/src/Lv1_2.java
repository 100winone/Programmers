/*
* 20201024 크레인 인형뽑기 게임 LV1
* */
import java.util.Stack;

public class Lv1_2 {
    public static void main(String[] args) {
        int[][] board = {{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}};
        int[] moves = {1, 5, 3, 5, 1, 2, 1, 4};
        int answer = solution(board, moves);
        System.out.println(answer);
    }

    public static int solution(int[][] board, int[] moves) {
        int answer = 0;
        int rowSize = board.length;
        Stack stack = new Stack();
        for (int i = 0; i < moves.length; i++) {
            int col = moves[i] - 1;
            for (int j = 0; j < rowSize; j++) {
                if (board[j][col] != 0) {
                    if (!stack.empty() && stack.peek().equals(board[j][col])) {
                        answer += 2;
                        stack.pop();
                    } else {
                        stack.push(board[j][col]);
                    }
                    board[j][col] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}



/*
import java.util.Stack;

public class Lv1_2 {
    public static void main(String[] args) {
        int[][] board = {{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}};
        int[] moves = {1, 5, 3, 5, 1, 2, 1, 4};
        int answer = solution(board, moves);
        System.out.println(answer);
    }

    public static int solution(int[][] board, int[] moves) {
        int answer = 0;
        int rowSize = board.length;
        Stack stack = new Stack();
        for (int i = 0; i < moves.length; i++) {
            int col = moves[i] - 1;
            for (int j = 0; j < rowSize; j++) {
               if (board[j][col] != 0) {
                    if (!stack.empty()) {
                        if (stack.peek().equals(board[j][col])) {
                            answer += 2;
                            stack.pop();
                        } else {
                            stack.push(board[j][col]);
                        }
                    } else {
                        stack.push(board[j][col]);
                    }
                    board[j][col] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}
*/
