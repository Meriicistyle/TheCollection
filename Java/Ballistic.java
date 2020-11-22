public class Ballistic {

    public static void main(String args[]) {
        double xzero = Double.parseDouble(args[0]);
        double vzero = Double.parseDouble(args[1]);
        double timez = Double.parseDouble(args[2]);
        double g = 9.81;

        double result = ((xzero + (vzero * timez)) - (g * (timez*timez) / 2));

        System.out.println(result);
    }
}