import java.util.Arrays;
import java.util.Scanner;

/**
 * B_Multiplication_Table
 */
public class B_Multiplication_Table {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    long[][] M = new long[n][n];
    for (int i = 0; i < M.length; i++) {
      for (int j = 0; j < M.length; j++) {
        M[i][j] = sc.nextInt();
      }
    }
    sc.close();

    long a02 = (long) M[1][0] * M[2][0] / M[2][1];

    System.out.print((int) Math.sqrt(a02) + " ");
    for (int i = 1; i < M.length - 1; i++) {
      long temp = M[i][0] * M[i][0] / a02;
      System.out.print((long) Math.sqrt(temp) + " ");
    }
    System.out.print((long) Math.sqrt(M[n - 1][0] * M[n - 1][0] / a02));
  }
}
