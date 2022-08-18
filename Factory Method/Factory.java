public class Factory{

    public static Computador createComputador(int tipoDeComputador){
        if (tipoDeComputador == 1){
            return new PC();
        } else if (tipoDeComputador == 2){
            return new Server();
        }
        else{
            return null;
        }

    }
}