public class Reverse2 {
    public static void main(String[] args) {
        for (int i = args.length - 1; i >= 0; i--) {
            for (int somz = args[i].length( ) - 1; somz >= 0; somz--) {
                System.out.print(args[i].charAt(somz));
            }
            System.out.print("");
        }
    }
}