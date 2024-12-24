package java_tutorial.exercise_4;

import java.util.Scanner;

/**
 *  programa que solicite al usuario ingresar un número e imprima si es positivo, negativo o cero.
 *
 *
 *  Modifica el programa para que el usario ingrese un número, y si es el 567043 imprime por pantalla
 *  "Has ganado el premio de Navidad". Sino imprime "Sigue jugando".
 */
public class Condicionales {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese un número: ");
        int numero = scanner.nextInt();

        if (numero > 0) {
            System.out.println("El número es positivo");
        } else if (numero < 0) {
            System.out.println("El número es negativo");
        } else {
            System.out.println("El número es cero");
        }
    }
}
