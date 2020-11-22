public class Random {

    public static void main(String args[]) {
        int lowerlimit = Integer.parseInt(args[0]);
        int upperlimit = Integer.parseInt(args[1]);

        int result = ((int)(Math.random() * ((upperlimit - lowerlimit) + 1)) + lowerlimit);
        System.out.println(result);
    }
}