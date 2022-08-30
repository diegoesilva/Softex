public class Mussarela extends SanduicheDeco {

    public Mussarela(Sanduiche sanduiche){
        super(sanduiche);
    }
    @Override
    public double informarPreco(){
        return super.informarPreco() + 2;
    }

    @Override
    public String informarIngredientes(){
        return super.informarIngredientes() + ", queijo mussarela";
    }
    
}