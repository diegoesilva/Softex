public class Carro extends Veiculo{

    public Carro(){
        this.modelo = "Fusca";
        this.marca = "Volkswagen";
        this.cor = "Branco";
        this.numeroRodas= 4;

    }
   
    @Override
    public Veiculo clone() {
        Carro novo = new Carro();
        
        novo.setModelo(this.modelo);
        novo.setMarca(this.marca);
        novo.setCor(this.cor);
        novo.setNumeroRodas(this.numeroRodas);

        return novo;

    }
   
}