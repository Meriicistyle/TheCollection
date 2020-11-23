public class TriangularNumbers {

    public static void main(String args[]) {
        int nthnum = Integer.parseInt(args[0]);

        // Gausssche Summenformel für Dreieckszahlberechnung  ---->  (n * (n + 1))/2   --- where n is the position we want.
        // Source: https://de.wikipedia.org/wiki/Dreieckszahl

        int i = 1;

        for (; i <= (nthnum * (nthnum + 1) / 2); i++) {
            if (i)
        }
    }
}