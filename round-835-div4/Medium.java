import java.util.Scanner;

/**
 * Medium
 */
public class Medium {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int count = sc.nextInt();
    for (int i = 0; i < count; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      int c = sc.nextInt();
    //   System.out.println(""+a+" "+b+" "+c);
    if((a>b && b>c) || (c>b && b>a)){
        System.out.println(b);
    }
    else if ( (b>a && a>c) || (c>a && a>b)) {
        System.out.println(a);
    }
    else{
        System.out.println(c);
    }
    }
  }
}
