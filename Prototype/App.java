public class App {
    
    public static void main(String args[]) { 
        
        /* Instanciando para preencher o vetor Venda*/
        Carro c1 = new Carro("Ka", "Ford", "Azul", 4);
        Carro c2 = new Carro("Uno", "Fiat", "Vermelho", 4);
        Carro c3 = new Carro();
        Bicicleta b1 = new Bicicleta("Émonda", "Trek", "Branca", 2);
        Bicicleta b2 = new Bicicleta("Cypress", "Giant", "Verde", 2);
        Bicicleta b3 = new Bicicleta();


        Veiculo Venda[] = {c1, c2, c3, b1, b2, b3}; /* Vetor a ser clonado */
        Veiculo cloneVenda[] = new Veiculo[6]; /* Vetor clone */

        for (int i=0; i<6; i++){
            cloneVenda[i] = Venda[i].clone(); /* Preenchendo vetor clone com clones*/
        }

        for (int i=0; i<6; i++){ /* Demonstrando objetos do vetor original e do vetor clone */
            System.out.println("Original: " + Venda[i] + " - Clone: " + cloneVenda[i]);
        }

    }

}

    

