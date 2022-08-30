public class App {

    public static void imprimirInfo(Sanduiche sand){
        System.out.println("Preço: $" + sand.informarPreco() + ", Ingredientes: " + sand.informarIngredientes());
    }

    public static void main(String[] args) {
        Sanduiche sand = new Frango();
        
        sand = new Pepperoni(sand);
        
        sand = new Mussarela(sand);
        imprimirInfo(sand);
    }
    
}
