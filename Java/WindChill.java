public class WindChill {

    public static void main(String args[]) {
        double timez = Double.parseDouble(args[0]);
        double velocity = Double.parseDouble(args[1]);

        double windcoldyy = 35.74 + 0.6215 * timez + (0.4275 * timez - 35.75) * Math.pow(velocity, 0.16);

        System.out.println(windcoldyy);
    }
}