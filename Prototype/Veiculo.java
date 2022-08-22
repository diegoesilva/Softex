public abstract class Veiculo{

    protected String modelo;
    protected String marca;
    protected String cor;
    protected int numeroRodas;
    

    protected abstract Veiculo clone();

    protected void setModelo(String modelo) {
        this.modelo = modelo;
    }

    protected void setMarca(String marca) {
        this.marca = marca;
    }

    protected void setCor(String cor) {
        this.cor = cor;
    }

    protected void setNumeroRodas(int numeroRodas) {
        this.numeroRodas = numeroRodas;
    }

}