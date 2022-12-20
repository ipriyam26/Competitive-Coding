import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * A_Cards
 */
public class A_Cards {

  // count of 1 will have one
  // count of 0 will have zero
  // we can find count of n in string and count of r in string and call it a day

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    String str = sc.next();

    int one = 0;
    int zero = 0;
    for (int i=0;i<str.length();i++) {
      if (str.charAt(i) == 'n') {
        one++;
      } else if (str.charAt(i) == 'z') {
        zero++;
      }
    }

    StringBuffer result = new StringBuffer();
    for (int i = 0; i < one; i++) {
      result.append("1");
      result.append(" ");
    }
    for (int i = 0; i < zero; i++) {
        result.append("0");
        result.append(" ");
    }
    System.out.println(result.toString().stripTrailing());
  }
}
