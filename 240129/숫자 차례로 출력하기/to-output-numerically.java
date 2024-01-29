import java.util.Scanner;

public class Main {
    static void printnum(int n, int i) {
        if(n == 0) {
            System.out.println();
            return;
        }
        System.out.print(i + " ");
        printnum(n-1, i + 1);
        System.out.print(i +" ");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 1;
        int n = sc.nextInt();
        printnum(n, i);
    }
}