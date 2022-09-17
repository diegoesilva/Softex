/* Considerando a solução apresentada no Hipertexto 5, aplique o padrão de projeto Strategy para criar uma
 simples calculadora. Os requisitos para avaliar o projeto são:
- implementar uma interface Strategy com o método abstrato execute(). Deve haver três classes concretas que
 implementam a Strategy para realizar as operações de Soma, Subtração e Multiplicação de números inteiros;
- o método execute() deve receber dois números inteiros como parâmetros e retornar o resultado também como 
número inteiro;
- como input do usuário, a aplicação deve receber o primeiro valor, depois o segundo e, por último, a 
operação matemática que deve realizar;
- no final, a aplicação deve definir qual Strategy será usada, com base na operação informada, e imprimir o
 resultado da operação.
*/

import java.io.*;

public class App{

    public static void main(String[] args) {

        Calculadora cal = new Calculadora();
        Console cnsl = System.console();


        System.out.println("Informe o primeiro número: ");
        int n1 = Integer.parseInt(cnsl.readLine());
        System.out.println("Informe o segundo número: ");
        int n2 = Integer.parseInt(cnsl.readLine());
        System.out.println("Informe a operação desejada: ");
        String op = cnsl.readLine();

        if (op.equals("+")){
            cal.setStrategy( new SomaStrategy());
        }
        else if (op.equals("-")){
            cal.setStrategy(new SubtracaoStrategy());
        }
        else if (op.equals("*")){
            cal.setStrategy(new MultiplicacaoStrategy());
        }

        int resultado = cal.executeStrategy(n1, n2);

        System.out.println("Resultado: " + resultado);
    }
}