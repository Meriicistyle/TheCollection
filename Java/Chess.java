public class Chess {

    public static void main(String[] args) {

        int thenumba = Integer.parseInt(args[0]);

        if (args.length == 0 || thenumba <= 0 ) {
            System.out.println("ERROR: TRY ENTERING SOMETHING VALID!");
            System.exit(0);
        }
        else if (args.length > 0) {
            for (int i = 1; i <= thenumba; i++) {
                for (int j = 1; j <= thenumba; j++) {
                    System.out.print("* ");
                }
                System.out.println();
            }
        }
    }
}