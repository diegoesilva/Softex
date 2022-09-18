public class PublisherConcreto extends Publisher{

    private String estado;

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
        notifyObservers();
    }


    
}
