package java_tutorial.exercise_6;

/**
 * Aplicación principla que crea un objeto Java, que representa algo del mundo real en Java.
 * En este caso crea una persoa, e invoca sus métodos.
 *
 * Tienes que crear una clase de tipo Empleado, que tenta los atributos "nombre" y "puesto".
 *
 * Implementa un método que sea "salario". Si el puesto es contable tiene que devolver "1.500 euros".
 * Si el puesto es "manager" tiene que que devolver "2.500 euros". Si es otro puesto tiene que devolver
 * "-1" (así indicamos que es un puesto no reconocido en la empresa).
 */
public class Aplicacion {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Juan";
        persona1.edad = 25;
        persona1.mostrarInformacion();
    }
}
