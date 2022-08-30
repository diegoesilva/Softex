public class Pepperoni extends SanduicheDeco {

    public Pepperoni(Sanduiche sanduiche){
        super(sanduiche);
    }
    @Override
    public double informarPreco(){
        return super.informarPreco() + 0.99;
    }

    @Override
    public String informarIngredientes(){
        return super.informarIngredientes() + ", pepperoni";
    }
    
}
