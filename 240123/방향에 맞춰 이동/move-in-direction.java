import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int x = 0, y = 0;
        int[] dx = new int[]{1,  0, -1, 0};
        int[] dy = new int[]{0, -1,  0, 1};
        Scanner sc  = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0 ; i < n; i++) {
            String d = sc.next();
            int k = sc.nextInt();

            if("E".equals(d)) {
                x += k*dx[0]; y += k*dy[0];
            }
            else if("S".equals(d)) {
                x += k*dx[1]; y += k*dy[1];
            }
            else if("W".equals(d)) {
                x += k*dx[2]; y += k*dy[2];
            }
            else {
                x += k*dx[3]; y += k*dy[3];
            }
        }
    System.out.print(x + " " + y);

    sc.close();

    }

}