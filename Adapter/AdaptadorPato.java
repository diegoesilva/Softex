public class AdaptadorPato implements Galinha{

    private Pato pato;

    public AdaptadorPato(Pato pato){
        this.pato = pato;
    }

    @Override
    public String fazerCocorico() {
        return pato.fazerQuaQua();
        
    }

    @Override
    public String voar() {
        return pato.voar();
        
    }

 
        


    

}
