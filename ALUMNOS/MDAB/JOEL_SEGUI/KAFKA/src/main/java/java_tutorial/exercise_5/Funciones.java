package java_tutorial.exercise_5;

/**
 * Define una función que tome dos parámetros y devuelva su suma.
 * Luego, utiliza esta función en el programa principal.
 *
 *
 * Implementa la función de la división e invócola como ya se hace para la función sumar.
 */
public class Funciones {
    public static void main(String[] args) {
        int resultado = sumar(3, 5);
        System.out.println("La suma es: " + resultado);
    }

    public static int sumar(int a, int b) {
        return a + b;
    }
}

