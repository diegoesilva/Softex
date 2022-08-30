public abstract class SanduicheDeco implements Sanduiche{
    private final Sanduiche SanduicheDeco;

    public SanduicheDeco(Sanduiche sanduiche){
        this.SanduicheDeco = sanduiche;
    }

    @Override
    public double informarPreco(){
        return SanduicheDeco.informarPreco();
    }
    
    @Override
    public String informarIngredientes(){
        return SanduicheDeco.informarIngredientes();
    }

    public Sanduiche getSanduiche(){
        return SanduicheDeco;
    }
    
}
